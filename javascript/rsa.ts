const BigInt = require('big-integer');

export const modulo = (a: number, b: number) => ((a % b) + b) % b;

export class Rsa {
    private p: number;
    private q: number;
    private e: number;
    private n: number;
    private phi: number;
    private d: number;

    public getPublicKey = () => [this.e, this.n];
    public getPrivateKey = () => [this.d, this.n];

    public egcd(a: number, b: number): [number, number, number] {
        if (a === 0) {
            return [b, 0, 1];
        }
        const [gcd, u, v] = this.egcd(b % a, a);
        return [gcd, v - Math.floor(b / a) * u, u];
    }

    public modinv(a: number, b: number): number {
        const [gcd, u] = this.egcd(a, b);
        if (gcd !== 1) {
            throw new Error("Module inverse doesn't exist");
        }
        return modulo(u, b);
    }

    public generateKeys(p: number, q: number, e: number): void {
        this.p = p;
        this.q = q;
        this.e = e;
        this.n = p * q;
        this.phi = (p - 1) * (q - 1);
        this.d = this.modinv(e, this.phi);
        if (this.phi % e === 0) {
            throw new Error("Invalid values for p and q");
        }
    }

    public encrypt(plaintext: string): number[] {
        const [e, n] = this.getPublicKey();
        const ciphered = [];
        for (const char of plaintext) {
            const code = char.charCodeAt(0);
            const cipheredCode = BigInt(code).modPow(e, n).toJSNumber();
            ciphered.push(cipheredCode);
        }
        return ciphered;
    }

    public decrypt(ciphered: number[]): string {
        const [d, n] = this.getPrivateKey();
        const plain = [];
        for (const cipheredCode of ciphered) {
            const code = BigInt(cipheredCode).modPow(d, n).toJSNumber();
            const char = String.fromCharCode(code);
            plain.push(char);
        }
        return plain.join("");
    }
}
