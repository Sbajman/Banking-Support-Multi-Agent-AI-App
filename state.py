from typing import TypedDict, Optional

class SupportState(TypedDict):
    user_message: str

    classification: Optional[str]
    sentiment: Optional[str]
    confidence: Optional[float]

    response_text: Optional[str]

    ticket_id: Optional[str]
    ticket_status: Optional[str]
    
    
    
    