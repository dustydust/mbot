class ValidatedEnum:

    @classmethod
    def __get_validators__(cls):
        yield cls.__validate_instance

    @classmethod
    def _validate_instance(cls, v):
        if v in cls.get_keys():
            return v
        else:
            raise ValueError("Invalid choice")