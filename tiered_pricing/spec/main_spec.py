from mamba import description, it
from expects import expect, be_true

with description('DummyClass') as self:
    with it('#dummy'):
        expect(True).to(be_true)
