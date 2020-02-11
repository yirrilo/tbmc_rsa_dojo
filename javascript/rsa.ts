const BigInt = require('big-integer');

export const modulo = (a: number, b: number) => ((a % b) + b) % b;

export class Rsa {
    private e: number;
    private n: number;
    private phi: number;
    private d: number;

    public getPublicKey = () => [this.e, this.n];
    public getPrivateKey = () => [this.d, this.n];

    public moduloInverse(a: number, b: number): number {
        throw new Error('not implemented');
    }

    public generateKeys(p: number, q: number, e: number): void {
        this.e = e;
        throw new Error('not implemented');
    }

    public encrypt(plaintext: string): number[] {
        throw new Error('not implemented');
    }

    public decrypt(ciphered: number[]): string {
        throw new Error('not implemented');
    }
}
