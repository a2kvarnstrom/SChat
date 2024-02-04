out = [
    {
        "uname": "wdjake",
        "salt": "0e02c80a52742b6635e5d108b9cfa16fa95f4199acf7155b25e67eccf460eef934491824267b967de5fac010793fac4a",
        "pass": "8529dedbde415e7b9b54e9788501f97f8dc929f266919901d2edf70cb1ff0de960733ee7d732dbbbe91e57e87184c2d566de95fe21e7dd730adda751bced0912"
    },
    {
        "uname": "test",
        "salt": "test",
        "pass": "64c37f15ca73f04d4ab34f6f9388dc63860e630efc3011def48c4e625c9c37616df5017df9461104b28aad2b874a5b464757398b83c24ba08eb57d57d9d83dfe"
    },
    {
        "uname": "a2kvarnstrom",
        "salt": "4dc24ff24e9d6767a025b7052beba47e1ba4fb101436eb72f447d84e935df0baea328deae6b655873dd2207f6876be21",
        "pass": "df2723ef1ae1f697cebdc5f67c213b793583fe3fc8ab835bab606355566770e16adfda70142b812ccdd240943e710f59295b10b529d15ca36ca8ae667f2d3a56"
    },
    {
        "uname": "sf",
        "salt": "9c06278568a9c9458586a674b3e15bd75fc53c0571f3a87f6f1865c1dd557acc7637cd3ca1eaa44748cea2e623026bbe",
        "pass": "215bac783dea9814c25d2d96c2b1145a1abf809075b416b6b8ed069c584d16476c0fd84cac4a2d94cee24b3d38e865e057b7373d31bb3ba9a11848d2b83b5d89"
    }
]

for i in range(len(out)):
    if out[i]["uname"] == "sf":
        print(i)
        print(out[i]["uname"])
        break
    elif out[i]["uname"] == "test":
        print(i)
        print(out[i]["uname"])
        break