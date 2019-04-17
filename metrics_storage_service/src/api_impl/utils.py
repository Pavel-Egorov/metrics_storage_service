import inspect
import logging
from uuid import uuid1

from django.conf import settings
from rest_framework import serializers
from wrapt import decorator

HIDE_ANNOTATION = 'hide'


class DynamicSerializer(serializers.Serializer):
    def get_fields(self):
        fields = super().get_fields()

        requested_fields = self.context['request'].query_params.get('fields')
        if not requested_fields:
            return fields

        filtered_fields = set(requested_fields.split(',')).intersection(fields)
        return {k: v for k, v in fields.items() if k in filtered_fields}


def get_logger(logger_name=settings.LOGGER_NAME):
    logger = logging.getLogger(logger_name)
    logger.propagate = False
    return logger


def log(logger_inst=get_logger(), lvl: int = logging.INFO, hide_output=False):
    @decorator
    def _log(wrapped, instance, args, kwargs):
        func_name = f'{wrapped.__module__}.{wrapped.__qualname__}'
        extra = {'call_id': uuid1().hex, 'function': func_name}

        try:
            params = inspect.getfullargspec(wrapped)
            extra['input_data'] = get_logged_args(params, [instance] + list(args) if instance else args, kwargs)
            logger_inst.log(level=lvl, msg=f'call {func_name}', extra=extra)

            result = wrapped(*args, **kwargs)

            extra['result'] = normalize_for_log(result) if not hide_output else 'hidden'
            logger_inst.log(level=lvl, msg=f'return {func_name}', extra=extra)
            return result
        except Exception as e:
            if hasattr(e, 'return_value'):
                return e.return_value

            raise

    return _log


def get_logged_args(params, args, kwargs):
    result = {}
    annotations = params.annotations

    for i, v in enumerate(args[:len(params.args)]):
        arg_name = params.args[i]
        result[arg_name] = 'hidden' if _is_hidden(arg_name, annotations) else normalize_for_log(v)

    varargs = params.varargs
    if varargs:
        if _is_hidden(varargs, annotations):
            result['*args'] = f'hidden {len(args) - len(params.args)} args'
        else:
            result['*args'] = [normalize_for_log(i) for i in args[len(params.args):]]

    for k, v in kwargs.items():
        is_kwarg_hidden = _is_hidden(k, annotations) or (
            params.varkw and k not in params.kwonlyargs and k not in params.args
        )
        result[k] = 'hidden' if is_kwarg_hidden else normalize_for_log(v)

    return result


def normalize_for_log(value):
    if isinstance(value, bool) or value is None:
        return str(value)
    elif isinstance(value, dict):
        return {k: normalize_for_log(v) for k, v in value.items()}
    elif isinstance(value, (list, set, frozenset, tuple)):
        return type(value)(normalize_for_log(i) for i in value)
    return str(value)


def _is_hidden(name, annotations):
    return annotations.get(name) == HIDE_ANNOTATION
