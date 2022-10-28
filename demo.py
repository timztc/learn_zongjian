import pandas as pd

df = pd.DataFrame(
    {
        "a": [{
            "t1": 1
        },
            {
                "t1": 2
        }
        ],

        "b":
        [
            11, 22
        ]
    }
)


# alist = df['a'].values.tolist()

# new_values = []

# for i in alist:
#     for k, v in i.items():
#         new_values.append(v)

# df['new_col'] = new_values

df['new_col'] = [cell['t1'] for cell in df['a']]


print(df)