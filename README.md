<div align="center">
 <img width="100%" src="https://user-images.githubusercontent.com/32566767/199652927-29a44fef-9b94-4d7c-84ff-3eb4e53e9655.png"/>
</div>


    Anyone can detect to slang in Korean sentence :)

<div align="center">
	<img src ="https://img.shields.io/badge/pypi-v0.1.0-blue"/>
	<img src ="https://img.shields.io/pypi/dm/koslang?color=light&style=flat-square"/>
</div>


## Insatllation
- ### PyPi Channel
```python
$ pip install koslang
```

## How to use

<details>
  <summary><b>isSlang()</b></summary>

  - `isSlang()` determines if the text contains Korean slang and returns true or false.
  - Params : sentence(str)
  - Returns : boolean (true / false)
```python
from koslang import koslang

koslang = koslang.koslang()

your_text = input()
print(koslang.isSlang(your_text))

# True / False
# print(koslang.isSlang("씨발")
# True
```

</details>


<details>
  <summary><b>analysis()</b></summary>

  - `analysis()` shows how the sentence was analyzed in detail in a list.
  - Params : sentence(str)
  - Returns : print(--Result of function--)
```python
from koslang import koslang

koslang = koslang.koslang()

your_text = input()
koslang.analysis(your_text)

# [result]


# koslang.analysis("이게 되네요.")
# ['이게', '되', '네요']
```

</details>

<details>
  <summary><b>showData()</b></summary>

  - `showData()` outputs in the form of a data frame that combines 5447 datasets built by itself and 13 data categories classified by them.
  - Params : x
  - Returns : printing our Dataset

    ```python
    from koslang import koslang
    
    koslang = koslang.koslang()
    koslang.showData()
    
    # print DataFrame
    # koslang.showData()
    #                prefix  suffix  interjection  ...  shape-shift  eroticism  specific
    # word_data                                ...                                  
    #  D쥐고             0       0             0  ...            0          0         0
    #  D지고             0       0             0  ...            0          0         0
    #  jot같            1       0             0  ...            0          0         0
    #  mi쳤             0       0             0  ...            0          0         0
    #  썅               0       0             1  ...            0          0         0
    #  ...           ...     ...           ...  ...          ...        ...       ...
    #  육갑하다            0       0             0  ...            0          0         0
    #  허섭스레기           0       0             0  ...            1          0         0
    #  띄발              1       0             1  ...            1          0         0
    #  쉬벨              1       0             1  ...            1          0         0
    #  쉬블              1       0             1  ...            1          0         0
    #
    # [5447 rows x 13 columns]
    ```

</details>


    Copyright 2022.11. Contributor(ash-hun, chaeha617, go-ring), All of contents cannot be copied without contributor's permission
