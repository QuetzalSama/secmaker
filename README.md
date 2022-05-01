# SecMaker 
A simple password generator by [Quetzal-sama](https://github.com/QuetzalSama).

## Requirements
* Python 3
    * Rich (optional)
    * Pyperclip (Optional)
    
## Usage
The basic syntax is the next
```bash
python3 main.py <length> <options>  
```
And the possible options are...
* Add numbers to the password
    ```bash
    -n <numbers>
    or
    --numbers <numbers>
    ```
* Add capital letters to the password
    ```bash
    -c <capital>
    or
    --capital <capital>
    ```
* Add lower letters to the password
    ```bash
    -l <lower>
    or
    --lower <lower>
    ```
* Add symbols to the password
    ```bash
    -s <symbols>
    or
    --symbols <symbols> 
    ```
* Add all stuff to the password, except symbols
    ```bash
    -a
    or
    --all 
    ```
* Use a password instead of a random one
    ```bash
    -p <password>
    or
    --password <password>
    ```

## Example
Make a 14-digit password with all options and don't use a random one
```bash
python3 main.py 14 --all --password Password123
```
The result will be `PASsWorD699orD`

Or make a random password with custom options...
```bash
python3 main.py 12 --numbers 4 --capital 2 --lower 4 --symbols 2
```
The result will be `E5w_ej4+Hx05`

Or create a password quickly by adding a symbol
```bash
python3 main.py -s 1
```
The result will be `X154@Hsqi7UbH7`

## Notes
* --numbers, --symbols, --capital, --lower, --all and --password are optional.
* --all is the default option if none is specified.
* --password is used to use a password instead of a random one, the length won't be ignored.
* --numbers, --symbols, --capital and --lower length are optional.
* the default length is 14.
* if you want to check if the password is strong, use the following [link](https://password.kaspersky.com/).
