class Pattern(object):
    """
    [summary]
    """
    @staticmethod
    def default() -> str:
        """[summary]

        Returns:
            pattern (str): [{level}][{datetime}] - {transaction} - {project_name}.{class_name}.{function_name} - _message: traceback
        """

        _message = "{message}"
        _title_pattern: str = "[{level}][{datetime}] - {transaction} - "
        _name_pattern: str = "{project_name}.{class_name}.{function_name} - "

        _loggger_pattern = f"{_title_pattern}{_name_pattern}{_message}"

        pattern = _loggger_pattern
        
        return pattern
