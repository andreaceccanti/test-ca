CERTIFICATE INVENTORY
=====================

apostrofe.cert.pem: 
    a certificate with an apostrophe in the subject

expired.cert.pem:
    an expired certificate

no_basic_constraints.cert.pem:
    a certificate missing the basic constraints extension.

dn_with_email.cert.pem:
	a certificate which has the deprecated emailAddress field in the subject.
	Note: the private key for this certificate is not encrypted.

no_key_usage.cert.pem:
    a certificate missing the key usage and extended key usage extensions.

revoked.cert.pem
    a revoked certificate.

test0.cert.pem,
test1.cert.pem,
test2.cert.pem,
test3.cert.pem,
test4.cert.pem,
test5.cert.pem:
    Five test certficates. 

three_spaces.cert.pem:
    a certificate with three spaces encoded in the last CN of the subject.

VO_Admin.cert.pem:
    a certificate that can be used as the VO admin for text fixture setup/teardown.
