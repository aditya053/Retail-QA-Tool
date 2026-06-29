few_shots = [
    {
        "input": "How many t-shirts do we have left for Nike in XS size and white color?",
        "sql_cmd": "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand='Nike' AND color='White' AND size='XS'",
        "sql_result": "[(0,)]",
        "answer": "There are no white Nike t-shirts available in extra-small (XS) size."
    },

    {
        "input": "How much is the total price of the inventory for all S-size t-shirts?",
        "sql_cmd": "SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size='S'",
        "sql_result": "[(16088,)]",
        "answer": "The total inventory value of all small-size t-shirts is ₹16,088."
    },

    {
        "input": "If we have to sell all the Levi's T-shirts today with discounts applied, how much revenue will our store generate?",
        "sql_cmd": """SELECT SUM(a.total_amount*((100-COALESCE(discounts.pct_discount,0))/100))
                        FROM (
                        SELECT SUM(price*stock_quantity) AS total_amount,
                        t_shirt_id
                        FROM t_shirts
                        WHERE brand='Levi'
                        GROUP BY t_shirt_id
                        ) a
                        LEFT JOIN discounts
                        ON a.t_shirt_id=discounts.t_shirt_id""",
                                "sql_result": "[(36880.2)]",
        "answer": "The store would generate ₹36,880.20 in revenue after applying discounts to all Levi's t-shirts."
    },

    {
        "input": "If we have to sell all the Levi's T-shirts today, how much revenue will our store generate without discount?",
        "sql_cmd": "SELECT SUM(price*stock_quantity) FROM t_shirts WHERE brand='Levi'",
        "sql_result": "[(17131,)]",
        "answer": "The store would generate ₹17,131 in revenue by selling all Levi's t-shirts without any discount."
    },

    {
        "input": "How many white color Levi's shirts do I have?",
        "sql_cmd": "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand='Levi' AND color='White'",
        "sql_result": "[(149,)]",
        "answer": "There are 149 white Levi's t-shirts available in stock."
    },

    {
        "input": "How much is the price of all white color Levi t-shirts?",
        "sql_cmd": "SELECT SUM(price*stock_quantity) FROM t_shirts WHERE brand='Levi' AND color='White'",
        "sql_result": "[(3207,)]",
        "answer": "The total inventory value of all white Levi's t-shirts is ₹3,207."
    }
]