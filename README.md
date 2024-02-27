
# Stock Data Analysis API

## Overview 🚀
This project, developed by Marcus Peterson, provides an API for fetching, processing, and analyzing stock data using advanced Python programming techniques, including FastAPI, PyTorch, and YFinance. It's designed to offer various endpoints for fetching raw and processed stock data, applying basic machine learning models, and plotting stock data trends.

## Features 🌟
- Fetch raw stock data from Yahoo Finance.
- Normalize and process stock data.
- Apply a simple PyTorch model for data analysis.
- Plot and return stock data trends as PNG images.
- Robust FastAPI endpoints for data fetching and processing.

## Installation 🛠️
To set up this project, you need to install the following dependencies:
```bash
pip install fastapi uvicorn matplotlib sklearn torch yfinance pandas
```

## Usage 💡
Run the application using Uvicorn:
```bash
uvicorn main:app --reload
```
Then, navigate to `http://127.0.0.1:8000` in your browser to interact with the API.

### Endpoints 🌐
1. **Raw Data**: `/data/{ticker}/{period}/{interval}`
2. **Normalized Data**: `/normalized-data/{ticker}/{period}/{interval}`
3. **Model-Applied Data**: `/model-data/{ticker}/{period}/{interval}`
4. **Plot Data**: `/plot/{ticker}/{period}/{interval}`

### Example Request
```bash
curl -X 'GET' 'http://127.0.0.1:8000/data/AAPL/month/1d' -H 'accept: application/json'
```

## Privacy Policy 📃
The API includes a privacy policy endpoint accessible at `/privacy-policy`.

## Contributing 🤝
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## Author 🖋️
Marcus Peterson

## License 📄
This project is open-sourced under the MIT License. See the LICENSE file for more information.

---

