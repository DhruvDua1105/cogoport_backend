from pydantic import BaseModel
from typing import Optional
class CountryConfigurationBase(BaseModel):
    """
    Pydantic schema representing the base fields of a country configuration.

    Attributes:
    - country_code (str): Country code of the country configuration.
    - business_name (str): Business name associated with the country configuration.
    - registration_number (str, optional): Registration number related to the country configuration.
    - additional_details (str, optional): Additional details specific to the country configuration.
    """
    country_code: str
    business_name: str
    registration_number: str = None
    additional_details: Optional[str] = None

class CountryConfigurationCreate(CountryConfigurationBase):
    """
    Pydantic schema for creating a new country configuration.

    Inherits from `CountryConfigurationBase`.
    """
    pass

class CountryConfigurationUpdate(CountryConfigurationBase):
    """
    Pydantic schema for updating an existing country configuration.

    Inherits from `CountryConfigurationBase`.
    """
    pass

class CountryConfiguration(CountryConfigurationBase):
    """
    Pydantic schema representing a country configuration including its ID.

    Inherits from `CountryConfigurationBase`.

    Attributes:
    - id (int): Primary key ID of the country configuration.
    """
    id: int

    class Config:
        orm_mode = True
