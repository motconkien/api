input string apiUrl = "http://127.0.0.1:5000/api/post_data";

void OnTick()
{
    for (int i = 0; i < OrdersTotal(); i++)
    {
        if (OrderSelect(i, SELECT_BY_POS))
        {
            string symbol = OrderSymbol();            // Get the trade symbol
            double openPrice = OrderOpenPrice();      // Get the open price
            double volume = OrderLots();              // Get the trading volume
            double marketPrice = (OrderType() == OP_BUY) ? Bid : Ask; // Get current market price
            double swap = OrderSwap();                // Get swap value
            double floatingPL = OrderProfit();        // Get floating profit/loss

            // Prepare JSON data
            string jsonData = "{\"symbol\":\"" + symbol + "\", \"open_price\":" + 
                              DoubleToString(openPrice, 5) + 
                              ", \"volume\":" + DoubleToString(volume, 2) + 
                              ", \"market_price\":" + DoubleToString(marketPrice, 5) + 
                              ", \"swap\":" + DoubleToString(swap, 2) + 
                              ", \"floating_pl\":" + DoubleToString(floatingPL, 2) + "}";

            // Send data to API
            char result[];
            string headers;
            int timeout = 5000; 
            int res = WebRequest("POST", apiUrl, headers, timeout, jsonData, result, headers);
            if (res == 200)
            {
                Print("Data sent successfully");
            }
            else
            {
                Print("Error sending data: ", GetLastError());
            }
        }
    }
}
