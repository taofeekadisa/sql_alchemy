from sqlalchemy import String, Table, Column, DateTime, Enum
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List
from datetime import datetime
from sqlalchemy import UniqueConstraint
import enum


class AdminRole(enum.Enum):
  super_admin = "super_admin"
  admin = "admin"
  user = "user" 

class AdminsDepartments(enum.Enum):
    sales = "sales"
    accounts = "accounts"
    logistics = "logistics"

class OrdersStatus(enum.Enum):
  pending = "pending"
  processing = "processing"
  shipped = "shipped"
  delivered = "delivered"
  confirmed = "confirmed"
  reviewed = "reviewed"
  canceled = "canceled"

class PayemntSatus(enum.Enum):
  pending = "pending"
  completed = "completed"
  failed = "failed"

class ShippingStatus(enum.Enum):
  pending = "pending"
  out_for_delivery = "out_for_delivery"
  lost = "lost"
  delivered = "delivered"

class ProductStatus(enum.Enum):
  in_stock = "in_stock"
  out_of_stock = "out_of_stock"
  low_stock = "low_stock"


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class Customer(Base):
    __tablename__ = "customers"

    first_name:Mapped[str] = mapped_column(String(30))
    last_name:Mapped[str] = mapped_column(String(30))
    username:Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    email:Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    phone_number:Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    password_hash:Mapped[str] = mapped_column(String(30))
    date_created:Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)
    
    order:Mapped[List["Order"]] = relationship(back_populates="customer")
    review:Mapped[List["Review"]] = relationship(back_populates="customer")
    address:Mapped[List["CustomerAddress"]] = relationship(back_populates="customer")
   
    def __repr__(self) -> str:
        return [f"Customer(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r},"
                f"username={self.username!r}, email={self.email!r}, phone_number={self.phone_number!r}, password_hash={self.password_hash!r},"
                f"date_created={self.date_created!r})"
                ]
    


class Vendor(Base):
    __tablename__ = "vendors"
    
    first_name:Mapped[str] = mapped_column(String(30))
    last_name:Mapped[str] = mapped_column(String(30))
    username:Mapped[str] =mapped_column(String(30), unique=True, nullable=False)
    email:Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    phone_number:Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    address:Mapped[str] = mapped_column(String(60))
    password_hash:Mapped[str] = mapped_column(String(30))
    date_created:Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)
    
    def __repr__(self) -> str:
        return [f"Vendor(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r},"
                f"username={self.username!r}, email={self.email!r}, phone_number={self.phone_number!r}, address={self.address!r},"
                f"password_hash={self.password_hash!r}, date_created={self.date_created!r})"
                ]
  
  
class Admin(Base):
    __tablename__ = "admins"
    
    first_name:Mapped[str] = mapped_column(String(30))
    last_name:Mapped[str] = mapped_column(String(30))
    username:Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    email:Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    phone_number:Mapped[str] =mapped_column(String(30), unique=True, nullable=False)
    department:Mapped[str] = mapped_column(Enum(AdminsDepartments))
    role:Mapped[str] = mapped_column(Enum(AdminRole))
    address:Mapped[str] = mapped_column(String(60))
    password_hash:Mapped[str] = mapped_column(String(30))
    date_created:Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)
    
    def __repr__(self) -> str:
        return [f"Admin(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r},"
                f"username={self.username!r}, email={self.email!r}, phone_number={self.phone_number!r}, address={self.address!r},"
                f"password_hash={self.password_hash!r}, department={self.department!r}, role={self.role!r}, date_created={self.date_created!r})"
                ]  
  
class Order(Base):
    __tablename__ = "orders"
    
    status:Mapped[str] = mapped_column(Enum(OrdersStatus))
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    created_at:Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)
    updated_at:Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)
    price:Mapped[float]
    
    order_item:Mapped[List["OrderItem"]] = relationship(back_populates="order")
    payment:Mapped["Payment"] = relationship(back_populates="order")
    shipping:Mapped[List["Shipping"]] = relationship(back_populates="order")
    customer:Mapped["Customer"] = relationship(back_populates="order")
    
    
    def __repr__(self) -> str:
        return [f"Order(id={self.id!r}, status={self.status!r}, customer_id={self.customer_id!r}, price={self.price!r},"
                f"created_at={self.created_at!r}, updated_at={self.updated_at!r})"]  
 
 
class OrderItem(Base):
    __tablename__ = "order_items"
    
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int]
    unit_price:Mapped[float]
    total_amt:Mapped[float]
    
    order:Mapped["Order"] = relationship(back_populates="order_item")
    product:Mapped["Product"] = relationship(backref="order_items")
    
    __table_args__ = (UniqueConstraint("product_id"),)
    
    
    def __repr__(self) -> str:
        return [f"OrderItem(id={self.id!r}, order_id={self.order_id!r}, product_id={self.product_id!r}, quantity={self.quantity!r},"
                f"unit_price={self.unit_price!r}, total_amt={self.total_amt!r})"]    

product_promotion = Table(
    "product_promotion",
    Base.metadata,
    Column("product_id", ForeignKey("products.id")),
    Column("promotion_id", ForeignKey("promotions.id")),
) 
        
class Product(Base):
    __tablename__ = "products"
    
    name:Mapped[str] = mapped_column(String(30))
    description:Mapped[str] = mapped_column()
    price:Mapped[float]
    catogory_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    vendor_id: Mapped[int] = mapped_column(ForeignKey("vendors.id"))
    status:Mapped[str] = mapped_column(Enum(ProductStatus))
    created_at:Mapped[DateTime] = mapped_column(DateTime, default=datetime.now) 
    updated_at:Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)
    image_url:Mapped[str] = mapped_column(String(100))
    
    vendor:Mapped["Vendor"] = relationship(backref="products")
    catogory:Mapped["Category"] = relationship(backref="products")
    review:Mapped["Review"] = relationship(back_populates="product")
    
    promotion: Mapped[List["Promotion"]] = relationship(
        secondary=product_promotion, back_populates="product")
    
    def __repr__(self) -> str:
        return [f"Product(id={self.id!r}, status={self.status!r}, description={self.description!r}, price={self.price!r},"
                f"catogory_id={self.category_id!r},vendor_id={self.vendor_id!r},"
                f"created_at={self.created_at!r}, updated_at={self.updated_at!r})"]
 
        
class Category(Base):
    __tablename__ = "categories"
    
    name:Mapped[str] = mapped_column(String(30))
    parentcategory:Mapped[str] = mapped_column(String(30))
    
    
    def __repr__(self) -> str:
        return [f"Category(id={self.id!r}, name={self.name!r}, parentcategory={self.parentcategory!r})"]
    

class Payment(Base):
    __tablename__ = "payments"
    
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    amount:Mapped[float]
    status:Mapped[str] = mapped_column(Enum(PayemntSatus))
    payment_method:Mapped[str] = mapped_column(String(50))
    transaction_id: Mapped[int]
    created_at:Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)
    
    order:Mapped["Order"] = relationship(back_populates="payment")
    
    __table_args__ = (UniqueConstraint("order_id"),)
    
    def __repr__(self) -> str:
        return [f"Payment(id={self.id!r}, order_id={self.order_id!r}, amount={self.amount!r},"
                f"status={self.status!r}, payment_method={self.payment_method!r}, transaction_id={self.transaction_id!r},"
                f"created_at={self.created_at!r})"]
        
class Cart(Base):
    __tablename__ = "carts"
    
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    
    customer:Mapped["Customer"] = relationship(backref="cart")
    
    __table_args__ = (UniqueConstraint("customer_id"),)
     
    def __repr__(self) -> str:
        return [f"Cart(id={self.id!r}, customer_id={self.customer_id!r})"]

    
class CartItem(Base):
    __tablename__ = "cart_items"
    
    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity :Mapped[int]
    
    def __repr__(self) -> str:
        return [f"CartItem(id={self.id!r}, product_id={self.customer_id!r}, quantity={self.quantity!r})"]
    
    
class Shipping(Base):
    __tablename__ = "shippings"
    
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    customer_address_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    shipment_status:Mapped[str] = mapped_column(Enum(ShippingStatus))
    tracking_id:Mapped[int]
    estimated_delivery:Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)
    
    order:Mapped["Order"] = relationship(back_populates="shipping")
     
    def __repr__(self) -> str:
        return [f"Shipping(id={self.id!r}, order_id={self.customer_id!r}, customer_address_id={self.customer_address_id!r},"
                f"shipment_status={self.shipment_status!r}, tracking_id={self.tracking_id!r}, estimated_delivery={self.estimated_delivery!r})"]
    
    
class CustomerAddress(Base):
    __tablename__ = "customer_addresses"
    
    residence_number:Mapped[int]
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    street:Mapped[str] = mapped_column(String(50))
    city:Mapped[str] = mapped_column(String(50))
    postal_code:Mapped[str] = mapped_column(String(50))
    country:Mapped[str] = mapped_column(String(50))
    description:Mapped[str] = mapped_column(String(50))
    
    customer:Mapped["Customer"] = relationship(back_populates="address")
    
    def __repr__(self) -> str:
        return [f"CustomerAddress(id={self.id!r}, residence_number={self.residence_number!r}, customer_id={self.customer_id!r},"
                f"street={self.street!r}, city={self.city!r}, postal_code={self.postal_code}, country={self.country!r})"]
        

class Inventory(Base):
    __tablename__ = "inventories"
 
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int]
    last_updated:Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)
 
    product:Mapped["Product"] = relationship(backref="inventories") 
    
    __table_args__ = (UniqueConstraint("product_id"),)
 
 
    def __repr__(self) -> str:
        return [f"Inventory(id={self.id!r},  product_id={self. product_id!r}, quantity={self.quantity!r},"
                f"last_updated={self.last_updated!r})"]

    
class Review(Base):
    __tablename__ = "reviews"
    
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    comment:Mapped[str] = mapped_column(String(50))
    rating: Mapped[int]
    created_at:Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)
    
    customer:Mapped["Customer"] = relationship(back_populates="review")  
    product:Mapped["Product"] = relationship(back_populates="review")
 
    def __repr__(self) -> str:
        return [f"Review(id={self.id!r},  product_id={self. product_id!r},  customer_id={self.customer_id!r},"
                f"comment={self.last_updated!r}, rating={self.rating!r}, created_at={self.created_at!r})"]
 
    
class Promotion(Base):
    __tablename__ = "promotions" 
    
    code:Mapped[str] = mapped_column(String(50))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    discount_percentage: Mapped[float]
    description:Mapped[str] = mapped_column(String(50))
    start_date:Mapped[DateTime] = mapped_column(DateTime)
    end_date:Mapped[DateTime] = mapped_column(DateTime)
    
    product: Mapped[List["Product"]] = relationship(
        secondary=product_promotion, back_populates="promotion")
    
    def __repr__(self) -> str:
        return (
        f"Promotion(id={self.id!r},product_id={self.product_id!r},code={self.code!r},"
        f"discount_percentage={self.discount_percentage!r},description={self.description!r},"
        f"start_date={self.start_date!r},end_date={self.end_date!r})"
    )
    
      