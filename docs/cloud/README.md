# Cloud hosting

If you want to host this app in the cloud there are some docs here for recommended ways to do that.

## Certificate generation

You will need to secure things using TLS (HTTPS) certificates.
Recommended: [Let's Encrypt](https://letsencrypt.org/).  
You can generate these using [certbot](https://certbot.eff.org/lets-encrypt/ubuntufocal-nginx).

### Certbot and just using nginx to create a cert only

These steps will just use nginx and certbot to generate the certificate.
You can then use the certificate in your cloud provider opr service of choice.

```bash
# install nginx, note this will turn on nginx as a service automatically. you may want to run this in a docker container
# to turn it off run:
# systemctl disable nginx
sudo apt install nginx

# install certbot
snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot

# Generate certificate, make sure your host name resolves (DNS) before running this.
certbot certonly --nginx
```