python3 -m pip --disable-pip-version-check --no-cache-dir --no-input install servicex-clients

date
echo "check rucio knows the node location"
python3 test_location.py

date
echo "xaod single variable no calculations to pandas df"
time python3 test_1.py

echo "xaod 8 variables from 2 collections to awkward array"
time python3 test_2.py

echo "xaod two variables simple filter to pandas df"
time python3 test_3.py

echo "xaod three variables from two collections adds a variable to awkward array"
time python3 test_4.py

echo "uproot single variable no calculations to pandas df"
time python3 test_101.py

echo "ALL DONE."