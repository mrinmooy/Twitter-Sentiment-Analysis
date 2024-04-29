package main

import (
    "database/sql"
    "fmt"
    "log"

    _ "github.com/go-sql-driver/mysql"
)

func main() {
   
    db, err := sql.Open("mysql", "sql5702693:HfQNBBzFVX@tcp(sql5.freesqldatabase.com:3306)/sql5702693")
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    
    if err := db.Ping(); err != nil {
        log.Fatal(err)
    }

   
    rows, err := db.Query("SELECT Sentiment, COUNT(*) FROM allTweets GROUP BY Sentiment")
    if err != nil {
        log.Fatal(err)
    }
    defer rows.Close()

    var sentiment int
    var count int
	fmt.Printf("There are ..\n")
    for rows.Next() {
        if err := rows.Scan(&sentiment, &count); err != nil {
            log.Fatal(err)
        }
        switch sentiment {
        case 0:
            fmt.Printf("%d positive tweets &,\n", count)
        case 1:
            fmt.Printf("%d negative tweets in the database.\n", count)
        }
    }

   
    if err := rows.Err(); err != nil {
        log.Fatal(err)
    }
}
