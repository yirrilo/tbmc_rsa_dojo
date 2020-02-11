const BigInt = require('big-integer');

export class Rsa {
    private e: number;
    private n: number;
    private phi: number;
    private d: number;

    public getPublicKey = () => [this.e, this.n];
    public getPrivateKey = () => [this.d, this.n];

    public moduloInverse(a: number, b: number): number {
        a = a % b;
        for (let i = 1; i < b; i++) {
            if ((a * i) % b === 1) {
                return i;
            }
        }
        return 1;
    }

    public generateKeys(p: number, q: number, e: number): void {
        this.e = e;
        this.n = p * q;
        this.phi = (p - 1) * (q - 1);
        this.d = this.moduloInverse(e, this.phi);
        if (this.phi % e === 0) {
            throw new Error('Invalid values for p and q');
        }
    }

    public encrypt(plaintext: string): number[] {
        const [e, n] = this.getPublicKey();
        const ciphered = [];
        for (const char of plaintext) {
            const code = char.charCodeAt(0);
            const cipheredCode = BigInt(code)
                .modPow(e, n)
                .toJSNumber();
            ciphered.push(cipheredCode);
        }
        return ciphered;
    }

    public decrypt(ciphered: number[]): string {
        const [d, n] = this.getPrivateKey();
        const plain = [];
        for (const cipheredCode of ciphered) {
            const code = BigInt(cipheredCode)
                .modPow(d, n)
                .toJSNumber();
            const char = String.fromCharCode(code);
            plain.push(char);
        }
        return plain.join('');
    }
}
