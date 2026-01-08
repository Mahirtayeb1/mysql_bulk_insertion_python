use coffee_shop_sales
DROP Table IF Exists coffee_sales;
CREATE TABLE coffee_sales(
	transaction_id Integer not null primary key,
    transaction_date varchar(10) not null,
    transaction_time varchar(8) not null,
    transaction_qty integer not null,
    store_id integer not null,
    store_location varchar(15) not null,
    product_id integer not null,
    unit_price numeric(5,2) not null,
    product_category varchar(18) not null,
    product_type varchar(21) not null,
    product_detail varchar(28) not null 
);

select * from coffee_sales;
select count(*) from coffee_sales;

-- show databases