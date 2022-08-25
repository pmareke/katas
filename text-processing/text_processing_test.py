from expects import equal, expect

from text_processing import TextProcessing


class TestTextProcessing:
    def test_process_text(self) -> None:
        input = """Hello, this is an example for you to practice. You should grab
        this text and make it as your test case.
        """
        expected = """Those are the top 10 words used:

1. this
2. you
3. hello
4. is
5. an
6. example
7. for
8. to
9. practice
10. should

The text has in total 21 words"""
        expect(TextProcessing().process(input)).to(equal(expected))

    def test_process_text_with_escapes(self) -> None:
        input = """Hello, this is an example for you to practice. You should grab
this text and make it as your test case:

```javascript
if (true) {
  console.log('should should should')
}
```"""
        expected = """Those are the top 10 words used:

1. this
2. you
3. hello
4. is
5. an
6. example
7. for
8. to
9. practice
10. should

The text has in total 21 words"""
        expect(TextProcessing().process(input, "```")).to(equal(expected))
