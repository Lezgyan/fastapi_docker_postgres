from typing import Final


class DiseaseNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Disease с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class DiseaseAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Disease с именем '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)



class CourseOfTreatmentNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Course of Treatment с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class CourseOfTreatmentAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Course of Treatment с уникальными параметрами уже существует"

    def __init__(self) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE
        super().__init__(self.message)


class DepartmentNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Department с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class DepartmentAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Department с именем '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class DoctorNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Doctor с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class DoctorAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Doctor с именем '{full_name}' уже существует"

    def __init__(self, full_name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(full_name=full_name)
        super().__init__(self.message)


class MedicineNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Medicine с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class MedicineAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Medicine с именем '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class PatientNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Patient с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class PatientAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Patient с уникальными данными уже существует"

    def __init__(self) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE
        super().__init__(self.message)



class WardNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Ward с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class WardAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Ward с именем '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)



class MedicalHistoryNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Medical History с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class MedicalHistoryAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Medical History с уникальными данными уже существует"

    def __init__(self) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE
        super().__init__(self.message)


class OperationNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Operation с id {id} не найдена"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class OperationAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Operation с уникальными параметрами уже существует"

    def __init__(self) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE
        super().__init__(self.message)


class OperationTypeNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Operation Type с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class OperationTypeAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Operation Type с именем '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class PatientReceptionNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Patient Reception с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class PatientReceptionAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Patient Reception с уникальными параметрами уже существует"

    def __init__(self) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE
        super().__init__(self.message)


class PositionNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Position с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class PositionAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Position с именем '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class QualificationDoctorNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Qualification Doctor с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class QualificationDoctorAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Qualification Doctor с уникальными параметрами уже существует"

    def __init__(self) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE
        super().__init__(self.message)


class QualificationTypeNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Qualification Type с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class QualificationTypeAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Qualification Type с именем '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class OperationToQualificationTypeNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Operation to Qualification Type с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class OperationToQualificationTypeAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Operation to Qualification Type с уникальными параметрами уже существует"

    def __init__(self) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE
        super().__init__(self.message)
