# Canadian Computing Competition (CCC) Solutions

This is used as a supplementary lesson material in my high school computer science classes.  It is a list of solutions that we implement as part of lessons.  We are as a class preparing to enter this competition and will produce these solutions in our preparations.  Feel free to contribute or collaborate on these.

## More information

Details about the competition can be found here:
[CCC Details](https://cemc.uwaterloo.ca/contests/computing/details.html)

## Problems we have solved

- 2019  
    - [x] [Problem J1: Winning Score](https://github.com/danielgunn/ccc/blob/master/y2019/j1.py)
    - [x] [Problem J2: Time To Compress](https://github.com/danielgunn/ccc/blob/master/y2019/j2.py)
    - [ ] Problem J3: Cold Compress
    - [ ] Problem J4/S1: Flipper
    - [ ] Problem J5: Rule of Three

## Testing

To run the test scripts, you can either:
- Use the Makefile (requires `wget` and `make` to be installed)
```bash
make test
```
-  OR, Follow the following steps:
1. first ensure the test data files have been extracted for each year to it's relevant directory.
    - extract [2019/all_data.zip](https://cemc.uwaterloo.ca/contests/computing/2019/stage%201/all_data.zip) to the y2019 folder.
    - ~~extract [2018/all_data.zip](https://cemc.uwaterloo.ca/contests/computing/2018/stage%201/all_data.zip) to the 2018 folder.~~
    - ~~extract [2017/all_data.zip](https://cemc.uwaterloo.ca/contests/computing/2017/stage%201/all_data.zip) to the 2017 folder.~~
2. run the test.py file
    ```bash
   python test.py 
   ```
