# check-key-images-ED25519
A Python script written to check if the double spend bug (in ed25519 curve) has been exploited in Bytecoin-based coins.


## Adapt to any currency based on Bytecoin (such as GotaNet)

Just change the daemon URL here:

[url = 'http://207.180.201.219:8081/json_rpc'](https://github.com/Gotanetwork/check-key-images-ED25519/blob/d7e2e9294864f086e6bf0c30c7a68d4e7e2044ff/double-spend.py#L23)

and change block height range as necessary here:

[range(1, 1267001)](https://github.com/Gotanetwork/check-key-images-ED25519/blob/d7e2e9294864f086e6bf0c30c7a68d4e7e2044ff/double-spend.py#L62)

## Bytecoin 

In the bytecoin network this bug was exploited, specifically in block #1243491. If you run this script in ```range(1243490, 1243492)``` this script create a file called ```bad_key_images``` **with key image**, **tx_hash** and **block height** as follows:

```
26e8958fc2b227b045c3f489f2ef98f0d5dfac05d3c63339b13802886d53fc05;cef289d7fab6e35ac123db8a3f06f7675b48067e0dff185c72b140845b8b3b23;1243491
```
The script also returns the following console output with more information:

```
====  block height 1243491 ====
tx: cef289d7fab6e35ac123db8a3f06f7675b48067e0dff185c72b140845b8b3b23
*** keyimage 26e8958fc2b227b045c3f489f2ef98f0d5dfac05d3c63339b13802886d53fc05 order 8
tx: 6945a25185da43dcc5d357194866df0ffdff12a6314af458629f6218ef4eb0eb
 - key image: c19fcf031ae9c72f718c5332bd30916be96e9e8efa8d1137dc6ca7ef6bdba412
 - key image: 3242b8a26bee44a9aef3cd0c790a50df4c629a77e05a779d4e15baac68c14d1c
tx: 58f0783b375a1286f70b4e32a5e0da57c4fa3dd4a6c82d142f2958d60d384e7e
 - key image: 9ea6ba59be12c6fd40d97cb657a20bc6b828b6a405282ebcaf498e105bcc626b
 - key image: 4382dcdfe1cf00490389979f8ca1befaa538ebf809a8b5a74649ecb1ea2c7701
tx: 13b1b190a4ea9a1e379267fb3588796b67a8b35b6567b28b02111e93e3ccee3e
 - key image: 419a5e444f5315f79f04ff82b5ea9666711b97e90a3f388ab0b5446a9c103467
 - key image: 7698334d57dd666c53605bccc5583585ef5abb2ab47f4e1427a46945fbc1f913
 - key image: 444cd9128edbe21961b4bb93b2ecc52b27ff6eba179eca44782fd39a1e5b7c6c
 - key image: 7810e8253108a2a28c3532192f2ece062a1a22b7611103a2e3e73409ca2ed380
tx: a2c38c8ec47cb4e9a553a215273a4b43969002130371624500f5e5505fa03962
 - key image: e91e6c59e706811b3d543e1fc1fa3c02fad88c344a2a2e7545c6f26118314dc5
 - key image: 43e9a8f1ae78beabcdbafa51d1ca0a375788ba142938307914d51e6ca7ce1823
 - key image: e5aaf2cda5c21dcb988caf459320534d1de43a041076195a185564cdb65457c5
 - key image: 80e26063686843812023ca8993d222c75fdbd705fe3016013911703563add799
 - key image: d90ea3db73fb15c1c5e8b6c4ac5c17ae2aaebeab302d23f7cb4556c042fe0223
tx: ae2a33ba05e5bdad38c7d8c46de80e72f15303f50ac1b8b86ae35a6fc361327c
 - key image: 7fd0471a5915d7969f26c8ec603d267304bbdc398e8c336244845adf887a30db
 - key image: 3c92510e7d8b74f50b85cb05fd9be5710591b45d95ded68f74a865e1108a0f96
 - key image: 6c0d572a7dee20aeba4cc429a5cfa8e03eeff81092a8c40c5fd64cac31843ccf
 - key image: e359a7c216a30e8304304731e23d4d1ec82165ed98a4918fdf33347a1828358f
 - key image: cdd4dbf997ea070a1d186e3cf1a3fea35ec5a04227b0a7c28f61e541c599bec3
 - key image: 34826a3f2fb2994e606d77ea45b749450d9a875f657d27b3e73df443bf49e608
tx: 32809809924231e8c994a70e6cbae4fa085812eafebb51aa9d6c0ab8f7902d5a
 - key image: 08f207ffa9c430a02b06a4283f9658793901c57840aec68849ac3f9773faa13f
 - key image: fcef9071ad4e19456a57439ee66049bb22fd5c3529040cefc86bda3aafc934f5
 - key image: bbd4277af327fde5cfbe84a3d96c631b9612f48e8fdc96641f6b7c835602e365
 - key image: 00ff60c5f984ce3312147615b58ef1c697fc7407753f5195e01868294b6d05dc
 - key image: e8716a983cb35ed37a749f2d220de0050e65ac54d691654ad8e92051bde14327
 - key image: 4a4eb37b5a51885f800c27b6ee93b2a7792c0d4b5900075367b41faa1381077c
 - key image: 6b757e6d972ced2fe0ebac5e88dfc3e7ff826eb8d4cfd34d26c978fbbaa1fc85
 - key image: a506fa671e197580a05eaf37144ac54fd90af7b8bbfec590d79cec6b06601f99
 - key image: a583b0f9f37179fe1e9128f6b36e5866b1a30c6bfd2567257f7ecc160fae5b6c
tx: 23e27bdc3279a55aa5f6be5106fa0d7a891d267297f98f3d8ba3ceeb84fdaf24
 - key image: f4a5a948673770153b1c72b876ef1207260c7879b105bfa0367174a1e7c9a1d9
 - key image: 27c288db7290b9cea1854cad6a480620c760a74ac4a5c24defb538d7ea00ffb6
 - key image: a20a9cb72cde222fe3cecfda0f480d1c9f24bc44022e3726c18042ebaeac03af
 - key image: fa716a5aa93a3f150a1a81056d41f194d69b50a6894d0774b82e7f4920a8ac8e
 - key image: 264c286779bb0f217903223244a917ebc666b0d7f3a1224fbe7030ad9b0fce39
 - key image: 42e8577ac16a4bf682ed2800dd65cbf0f23ae79c3a7462aae93e12c0df002c03
 - key image: 37d79611e26413d187b95138197216f4ffb0781b29ef10c265e851403cce3652
 - key image: 379f877236b00fdc5fc0bb6090bc044fe40c415332477a22495f1250234e9753
 - key image: 9b9f52418b30d16e9dce5ccd8b9bb198b5615d242546bfda923d0c414698c98e
 - key image: b877638fafaa7cc72c77a16255ee415a26de89d416dba5610b96fdd2d1a7f39c
 ```
 
#### Sources:

[getmonero.org 2017/05/17](https://www.getmonero.org/2017/05/17/disclosure-of-a-major-bug-in-cryptonote-based-currencies.html)

[getmonero.org 2018/09/25](https://www.getmonero.org/2018/09/25/a-post-mortum-of-the-burning-bug.html)

[monero.stackexchange.com How does the recent patched key image exploit work in practice?](https://monero.stackexchange.com/questions/4241/how-does-the-recent-patched-key-image-exploit-work-in-practice)
