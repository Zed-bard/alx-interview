
# 0x03. Log Parsing

This project contains interview coding challenges focused on log parsing.

## Tasks To Complete

### 0. Log parsing

[0-stats.py](0-stats.py) contains a script that reads `stdin` line by line and computes metrics:

#### Input Format:
```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```
- If the format is not as above, the line will be skipped.

#### Functionality:
- After every 10 lines and/or a keyboard interruption (`CTRL + C`), the script prints the following statistics from the beginning:
  - **Total file size:** 
    ```
    File size: <total size>
    ```
    Where `<total size>` is the sum of all previous `<file size>` values.
  - **Number of lines by status code:**
    - Possible status codes: `200`, `301`, `400`, `401`, `403`, `404`, `405`, `500`.
    - If a status code doesn’t appear or is not an integer, it will not be printed.
    - Format:
      ```
      <status code>: <number>
      ```
    - Status codes are printed in ascending order.

## How to Run

To run the script, use the following command:
```bash
python3 0-stats.py
```

The script will continuously read from `stdin` until interrupted.

## Example

Given the following input:
```
10.0.0.1 - [2023-07-01] "GET /projects/260 HTTP/1.1" 200 1024
10.0.0.2 - [2023-07-01] "GET /projects/260 HTTP/1.1" 301 2048
10.0.0.3 - [2023-07-01] "GET /projects/260 HTTP/1.1" 200 1024
10.0.0.4 - [2023-07-01] "GET /projects/260 HTTP/1.1" 404 512
10.0.0.5 - [2023-07-01] "GET /projects/260 HTTP/1.1" 500 1024
10.0.0.6 - [2023-07-01] "GET /projects/260 HTTP/1.1" 200 256
10.0.0.7 - [2023-07-01] "GET /projects/260 HTTP/1.1" 403 512
10.0.0.8 - [2023-07-01] "GET /projects/260 HTTP/1.1" 301 1024
10.0.0.9 - [2023-07-01] "GET /projects/260 HTTP/1.1" 200 2048
10.0.0.10 - [2023-07-01] "GET /projects/260 HTTP/1.1" 200 512
```

The output after 10 lines will be:
```
File size: 9984
200: 5
301: 2
403: 1
