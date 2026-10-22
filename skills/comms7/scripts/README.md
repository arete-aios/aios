# COMMS7 helper

Parent: [SKILL.md](../SKILL.md). [review_pack.py](review_pack.py) is the optional
offline Python3 packer. Read the [input contract](../references/PYTHON-HELPER.md)
when using structured JSON. It makes no network calls or account changes.

[Offline behaviour tests](test_review_pack.py) check retained open work, account identity, conflicts and decision evidence without contacting an account. Run `python3 -B scripts/test_review_pack.py`.
