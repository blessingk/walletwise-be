from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.db.database import Base


class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    plan_name = Column(String)
    stripe_subscription_id = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime, nullable=True)
    status = Column(Enum("active", "canceled", "paused", name="subscription_status"))

    user = relationship("User", back_populates="subscriptions")
