import * as RsaModule from "./rsa";

describe("modulo", function() {
    it.each`
        a     | b     | expected
        ${-9} | ${23} | ${14}
    `("should return $expected when a is $a, b is $b", ({ a, b, expected }) => {
        const result = RsaModule.modulo(a, b);
        expect(result).toEqual(expected);
    });
});

describe("RsaModule", () => {
    let rsa: RsaModule.Rsa;

    beforeEach(() => {
        rsa = new RsaModule.Rsa();
        rsa.generateKeys(11, 13, 7);
    });

    describe("egcd", () => {
        it.each`
            a      | b     | expectedGcd
            ${120} | ${23} | ${1}
            ${240} | ${46} | ${2}
        `("should return $expectedGcd when a is $a, b is $b", ({ a, b, expectedGcd }) => {
            const [gcd, u, v] = rsa.egcd(a, b);
            expect(gcd).toEqual(expectedGcd);
            expect(a * u + b * v).toEqual(expectedGcd);
        });
    });

    describe("modinv", () => {
        it.each`
            a      | b     | expectedModInv
            ${120} | ${23} | ${14}
        `("should return $expectedModInv when a is $a, b is $b", ({ a, b, expectedModInv }) => {
            const modinv = rsa.modinv(a, b);
            expect(modinv).toEqual(expectedModInv);
        });

        it("should throw when gcd is not 1", () => {
            expect(() => rsa.modinv(240, 46)).toThrow();
        });
    });

    it("should have good public key", () => {
        expect(rsa.getPublicKey()).toEqual([7, 143]);
    });

    it("should have good private key", () => {
        expect(rsa.getPrivateKey()).toEqual([103, 143]);
    });

    it('should encrypt', () => {
        const ciphered = rsa.encrypt("my text");
        expect(ciphered).toEqual([21, 121, 98, 129, 62, 120, 129]);
    });

    it('should decrypt', () => {
        const plaintext = rsa.decrypt([21, 121, 98, 129, 62, 120, 129]);
        expect(plaintext).toEqual("my text");
    });

    it("should encrypt then decrypt 'my text'", () => {
        const text = "my_text";
        const ciphered = rsa.encrypt(text);
        const plaintext = rsa.decrypt(ciphered);
        expect(plaintext).toEqual(text);
    });
});
