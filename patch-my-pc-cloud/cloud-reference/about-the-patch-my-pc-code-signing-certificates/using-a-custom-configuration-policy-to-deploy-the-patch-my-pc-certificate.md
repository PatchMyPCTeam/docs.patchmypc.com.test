# Using a Custom Configuration Policy to deploy the Patch My PC certificate

_Applies to: Patch My PC Cloud_

Our recommended method for deploying Patch My PC (PMPC) code signing certificates is to use a custom configuration policy.

This method uses the base64 encoded representation of the certificate and deploys it using a custom configuration profile.

To deploy the certificate using a custom configuration policy, follow the [Create a profile with custom settings in Intune](https://learn.microsoft.com/en-us/mem/intune/configuration/custom-settings-configure) article using the following values.

### Certificates to Deploy

There are two distinct use cases in PMPC Cloud that require separate certificates:

1. [Intune Detection and Requirement Scripts](using-a-custom-configuration-policy-to-deploy-the-patch-my-pc-certificate.md#deploy-the-certificate-use-to-sign-intune-detection-and-requirement-scripts)\
   Used to sign **Intune detection and requirement scripts** for Win32 applications published through PMPC Cloud.&#x20;
2. [Patch My PC Helper Scripts](using-a-custom-configuration-policy-to-deploy-the-patch-my-pc-certificate.md#deploy-the-certificate-use-to-sign-patch-my-pc-helper-scripts)\
   Used to sign required and recommended pre/post "helper" scripts for certain applications in the PMPC catalog. These helper scripts perform essential tasks such as stopping processes, uninstalling older software versions, or configuring application behavior during deployment to ensure successful app installation.

## 1. Deploy the Certificate use to sign Intune Detection and Requirement Scripts

### “Create a Profile” tab&#x20;

<table><thead><tr><th width="139">Field</th><th width="218">Value</th></tr></thead><tbody><tr><td>Platform</td><td>Windows 10 and later</td></tr><tr><td>Profile type</td><td>Templates > Custom</td></tr></tbody></table>

### “Basics” tab&#x20;

<table><thead><tr><th width="140">Field</th><th>Value</th></tr></thead><tbody><tr><td>Name</td><td>A descriptive name for the policy. E.g. “Patch My PC Cloud Trusted Publisher Certificate”`</td></tr><tr><td>Description</td><td>Enter an optional description for the policy</td></tr></tbody></table>

### “Configuration Settings” tab

<table><thead><tr><th width="135">Field</th><th>Value</th></tr></thead><tbody><tr><td>Name</td><td>Enter a descriptive name for the OMA-URI setting e.g. “Patch My PC Cloud Trusted Publisher Certificate”</td></tr><tr><td>Description</td><td>Enter an optional description for the policy</td></tr><tr><td>OMA-URI</td><td>./Device/Vendor/MSFT/RootCATrustedCertificates/TrustedPublisher/E2806E45DDA692221BED082D072BAF5973FBC466/EncodedCertificate</td></tr><tr><td>Data type</td><td>String</td></tr><tr><td>Value</td><td>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</td></tr></tbody></table>

### “Scope tags” tab

Configure as required.

### “Assignments” tab

Assign the configuration template to the desired Entra ID group(s).

### “Applicability Rules” tab

Configure any desired applicability rules.

### “Review + create” tab

Double-check everything before clicking **Create**.

## 2. Deploy the Certificate use to sign Patch My PC Helper Scripts&#x20;

### “Create a Profile” tab&#x20;

| Field        | Value                |
| ------------ | -------------------- |
| Platform     | Windows 10 and later |
| Profile type | Templates > Custom   |

### “Basics” tab&#x20;

<table><thead><tr><th width="142">Field</th><th>Value</th></tr></thead><tbody><tr><td>Name</td><td>A descriptive name for the policy. E.g. “Patch My PC Apps Trusted Publisher Certificate”`</td></tr><tr><td>Description</td><td>Enter an optional description for the policy</td></tr></tbody></table>

### “Configuration Settings” tab

<table><thead><tr><th width="135">Field</th><th>Value</th></tr></thead><tbody><tr><td>Name</td><td>Enter a descriptive name for the OMA-URI setting e.g. “Patch My PC Apps Trusted Publisher Certificate”</td></tr><tr><td>Description</td><td>Enter an optional description for the policy</td></tr><tr><td>OMA-URI</td><td>./Device/Vendor/MSFT/RootCATrustedCertificates/TrustedPublisher/0FE8270B04362770B4D926D75E118B41A10545E8/EncodedCertificate</td></tr><tr><td>Data type</td><td>String</td></tr><tr><td>Value</td><td>MIIHyTCCBbGgAwIBAgIQDMNw87U7UZ48Hv1za61jojANBgkqhkiG9w0BAQsFADBpMQswCQYDVQQGEwJVUzEXMBUGA1UEChMORGlnaUNlcnQsIEluYy4xQTA/BgNVBAMTOERpZ2lDZXJ0IFRydXN0ZWQgRzQgQ29kZSBTaWduaW5nIFJTQTQwOTYgU0hBMzg0IDIwMjEgQ0ExMB4XDTIzMDQwNzAwMDAwMFoXDTI2MDQzMDIzNTk1OVowgdExEzARBgsrBgEEAYI3PAIBAxMCVVMxGTAXBgsrBgEEAYI3PAIBAhMIQ29sb3JhZG8xHTAbBgNVBA8MFFByaXZhdGUgT3JnYW5pemF0aW9uMRQwEgYDVQQFEwsyMDEzMTYzODMyNzELMAkGA1UEBhMCVVMxETAPBgNVBAgTCENvbG9yYWRvMRQwEgYDVQQHEwtDYXN0bGUgUm9jazEZMBcGA1UEChMQUGF0Y2ggTXkgUEMsIExMQzEZMBcGA1UEAxMQUGF0Y2ggTXkgUEMsIExMQzCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAKaQcs40YzBFv5HXQFPd04rKJ4uBdwvAZLKuULy+icZOpgs/Sy329Ng5ikhB5o1IdvE2cOT20sjs3qgb4e+rqs7taTCe6RNLsDINsmcTlp4yxOfV80EZ08ld3o36GEgH0Vy1vrJXLTRKNULzV7gIzF/e3tO1Fab4IxKZNcBSXiv8ORqcgT9O7/RZoqyG87iU6Q/dKfC4WzvU396XJ3FMZrI+s4CgV8p6pVNjijBjH7pmzoXynFtA0j6NH6tg4DmQvm+kfWXtWbDpPYhdFz1gccJt1DjTrJetpIwBzDAS8NGA75HQhBmQ3gcnNDJLgylB3HyWOeXS+vxXR0Pi/W419cfn8zCFH0u2O4QFaZsT2HoIE/t9EhdAKdHoKwvVoCgwvlx3jjwFq5MnoB2oJiNmTGQyhiRvCaw6JACKUa43eJvlRKylEy4INDTOX5BeivJoTqCw0cCAd6ZuRh6gRl8shIVfN78qunQqJZQkDimtQY5Sn33w+ee5/lFSxOxBg6iu7vCGPZ6QxJd6oVdRa8t87vJ4QVlsMQQRa400S7kqIX1HOnbR3hxgvcks8kBRMYtZ8g3Fz/WTCW5sWbExVpn6HC6DsRhosF/DBGYmIqQJz6odkCFCr7QcmpGjoZs4jRDegSC5utEusBYmvCfVxtud3R43WEdCRfHuD1OFDm5HoonnAgMBAAGjggICMIIB/jAfBgNVHSMEGDAWgBRoN+Drtjv4XxGG+/5hewiIZfROQjAdBgNVHQ4EFgQU3wgET0b7maQo7OF3wwGWm83hl+0wDgYDVR0PAQH/BAQDAgeAMBMGA1UdJQQMMAoGCCsGAQUFBwMDMIG1BgNVHR8Ega0wgaowU6BRoE+GTWh0dHA6Ly9jcmwzLmRpZ2ljZXJ0LmNvbS9EaWdpQ2VydFRydXN0ZWRHNENvZGVTaWduaW5nUlNBNDA5NlNIQTM4NDIwMjFDQTEuY3JsMFOgUaBPhk1odHRwOi8vY3JsNC5kaWdpY2VydC5jb20vRGlnaUNlcnRUcnVzdGVkRzRDb2RlU2lnbmluZ1JTQTQwOTZTSEEzODQyMDIxQ0ExLmNybDA9BgNVHSAENjA0MDIGBWeBDAEDMCkwJwYIKwYBBQUHAgEWG2h0dHA6Ly93d3cuZGlnaWNlcnQuY29tL0NQUzCBlAYIKwYBBQUHAQEEgYcwgYQwJAYIKwYBBQUHMAGGGGh0dHA6Ly9vY3NwLmRpZ2ljZXJ0LmNvbTBcBggrBgEFBQcwAoZQaHR0cDovL2NhY2VydHMuZGlnaWNlcnQuY29tL0RpZ2lDZXJ0VHJ1c3RlZEc0Q29kZVNpZ25pbmdSU0E0MDk2U0hBMzg0MjAyMUNBMS5jcnQwCQYDVR0TBAIwADANBgkqhkiG9w0BAQsFAAOCAgEADaIfBgYBzz7rZspAw5OGKL7nt4eo6SMcS91NAex1HWxak4hX7yqQB25Oa66WaVBtd14rZxptoGQ88FDezI1qyUs4bwi4NaW9WBY8QDnGGhgyZ3aT3ZEBEvMWy6MFpzlyvjPBcWE5OGuoRMhP42TSMhvFlZGCPZy02PLUdGcTynL55YhdTcGJnX0Z2OgSaHUQTmXhgRX+fajIilPnmmv8Av4Clr6Xa9SoNHltA04JRiCu4ejDGFqA94F696jSJ+AUYHys6bnPc0E8JB9YnFCAurPRG8YBJAofUtxnGIHGE0EiQTZeXf0nKmVBIXkE3hT4mZx7pH7wrlCr0FV4qnq6j0uaj4oKqFbkdyzb5u+XQe9pPojshnjVzhIRK53wsGaFP4gSURxWvcThIOyoaKrVDZOdLQZXEz8Anks3Vs5XscjyzFR7pv/3Reik7FaZRTvd5rDW6foDJOiCwX5p+UnldHGHW83rDvtks1rwgKwuuxvCG3Bkjirl94EImpiugGaRQ7S2Lydxpqzv7Hng4YQbIIvVMNC7mNrVZPNWdF4/a9yjDt2nJrnRcDK1zvHBXSrAYIycQ6hhhlHS9Y4MRhz35t1du/Y0IXDB7HBYSvcsrpxtBzXLTd2NCNCtdkwYIl7WTQeoCbZWvo4PbzJBOnPjs1tN4upe9XomxtZkNAwIOfM=</td></tr></tbody></table>

### “Scope tags” tab

Configure as required.

### “Assignments” tab

Assign the configuration template to the desired Entra ID group(s).

### “Applicability Rules” tab

Configure any desired applicability rules.

### “Review + create” tab

Double-check everything before clicking **Create**.

## Post Processing

Once the client processes the policy, the certificate appears as follows in its **Trusted Publishers** store.

![](/_images/image-(654 "").png "")

Double-clicking the certificate allows you to see its properties.

![](/_images/image-(655 "").png "")
