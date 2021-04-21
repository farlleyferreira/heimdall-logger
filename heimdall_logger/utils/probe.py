

from typing import List, Tuple
from inspect import FrameInfo


class Probe(object):
    """
    [summary]
    """

    @staticmethod
    def inspect_namespaces_from(stack: List[FrameInfo]) -> Tuple[str, str]:
        """[summary]

            Args:
                stack (List[FrameInfo]): [description]

            Returns:
                Tuple[str, str]: [description]
            """

        frame = stack[1]
        frame_info = frame[0]

        self_object = frame_info.f_locals.get(
            'self',
            None
        )

        class_name = self_object.__class__.__name__ if self_object else frame[1]
        function_name = frame[3]

        return class_name, function_name
