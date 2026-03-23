# 🏀 NBA Player Stats Scraper

This project is a Python-based web scraping tool that extracts NBA player statistics from the official NBA website and saves the data into a CSV file for further analysis.

The script uses Selenium to automate browser actions and dynamically scrape data from the stats section.

---

## 🚀 Features

* 🌐 Automated navigation of the NBA website
* 📊 Extracts player statistics from dynamic tables
* 🧾 Saves structured data into CSV format
* ⚡ Handles dynamic content loading using WebDriverWait
* 🤖 Fully automated scraping process

---

## 🛠️ Technologies Used

* Python 🐍
* Selenium 🌐
* CSV (Built-in module) 📄

---

## 📂 Project Structure

```id="c2k91s"
project-folder/
│
├── main.py
├── nba_stats.csv   # Output file
└── README.md
```

---

## ⚙️ How It Works

1. Opens the NBA website using Selenium:

   ```
   https://www.nba.com/
   ```

2. Navigates to:

   * Stats section
   * Players tab
   * Traditional Stats page

3. Waits for elements to load dynamically

4. Extracts:

   * Player Name
   * Team
   * Points, Assists, Rebounds
   * Shooting percentages
   * And more stats...

5. Stores all extracted data into a CSV file

---

## ▶️ How to Run

### 1. Clone the repository

```bash id="k1m9sx"
git clone https://github.com/your-username/nba-stats-scraper.git
cd nba-stats-scraper
```

### 2. Install dependencies

```bash id="n8q2pl"
pip install selenium
```

### 3. Setup ChromeDriver

* Download ChromeDriver matching your browser version
* Add it to your system PATH

---

### 4. Run the script

```bash id="u2l0zp"
python main.py
```

---

## 📊 Output

* The script generates a file:

  ```
  nba_stats.csv
  ```

* Contains:

  * Rank
  * Player Name
  * Team
  * Games Played
  * Points (PTS)
  * Assists (AST)
  * Rebounds (REB)
  * Shooting percentages
  * And more...

---

## ⚠️ Important Notes

* Website structure may change → XPath may need updates
* Internet connection required
* Page loading delays are handled using `WebDriverWait`
* Ensure Chrome browser is installed

---

## 🧠 Challenges Handled

* Dynamic content loading
* Pop-up handling (cookies)
* Table extraction from complex HTML structure

---

## 🚀 Future Improvements

* Add pagination support (scrape all pages)
* Export data to Excel or database
* Add filters (team-wise, player-wise)
* Build dashboard for visualization

---

## 👨‍💻 Author

Karthikeyan

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
