# ERC 20 - OpenZeppelin Akıllı Kontratı ile Ethereum Tabanlı Token Oluşturmak

Ethereum geliştirmek için kullanılan bazı bir takım frameworkler bulunmakta ancak bunlar hem meşakatli hemde yüksek gereksinimleri bulunmakta (Etc zinciri- RPC sunuc vs.)
Bu işlemlerin minimize edinmesi açısından etc-brownie framework kullanarak basit bir ISTANBUL Token isimli kripti birimi oluşturdum.

Test sunucu üzerindeki varlığı ve kontrat bilgilerini görüntülemek isterseniz --> https://kovan.etherscan.io/token/0x8b3783b6d61bc086abf875616c280c5b004eb8af

## Gereksinimler  
Kullanımdan önce lütfen aşağıdakileri kurun ve kurulum yönergelerini takip edin : 

- [nodejs and npm](https://nodejs.org/en/download/)
- [python](https://www.python.org/downloads/)

## Kurulum

1. [Brownie Kuruluımu](https://eth-brownie.readthedocs.io/en/stable/install.html), Eğer gerekli okumayı yaptıysanız kuruluma başlayalım! Ayrıca gerekli geliştirme parametreleri ve yönergeleri okumanızda fayda var. import kısımları ve cüzdan bakiyesi gibi gerekli fonksiyonları öğrenin.

```bash
pip install eth-brownie
```
Yada, çalıştırmadıysanız pipx ile kurulum : 
```bash
pip install --user pipx
pipx ensurepath
# terminalinizi yeniden başlatın
pipx install eth-brownie
```

Şimdi ki aşamamız brownie üzerinden tokenizin özelliklerini belirtmek. Bunun için;

- build
	- contracts
	- interfaces
	- reports
	- scripts
		-1_deploy_token.py   --> Ben özelliklerini burda belirttim sizde istediğiniz değişikliği yapabilir ya brownie rehberine göre farklılaştırabilirsiniz.
	- tests



Çalıştırmak için : brownie run scripts/1_deploy_token.py  --network kovan

