# About the Patch My PC Code-Signing Certificates

_Applies to: Patch My PC Cloud_

Patch My PC (PMPC) signs PowerShell scripts with a code-signing certificate from a public Certificate Authority (CA). The following scripts are code-signed:

* Intune Win32 app Detection Scripts
* Intune Win32 app Requirement Scripts
* Patch My PC helper Scripts used in certain Catalog apps

For these scripts to run correctly under an [AllSigned](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4) execution policy, the public key of the code-signing certificate(s) must be present in the **Trusted Publishers** certificate store on all relevant computers you intend to deploy the packages to.

If this public key is not in the store, scripts will fail to execute. No error will be thrown in the log files, however, **powershell.exe** will hang while it tries to execute the detection or requirement script.

### Certificates used

There are two distinct use cases that require separate certificates in Patch My PC:

1. [Intune Detection and Requirement Scripts](./#use-case-1-intune-detection-and-requirement-scripts)\
   Used to sign **Intune detection and requirement scripts** for Win32 applications published through PMPC Cloud.
2. [Patch My PC Helper Scripts](./#use-case-2-patch-my-pc-helper-scripts)\
   Used to sign required and recommended pre/post "helper" scripts for certain applications in the PMPC catalog. These helper scripts perform essential tasks such as stopping processes, uninstalling older software versions, or configuring application behavior during deployment to ensure successful app installation.

> **Important**
>
> Patch My PC **only** signs helper scripts that we author for certain applications in the PMPC catalog. Any customer-provided scripts added using the \[Cloud "Scripts" Deployment Tool]\(../../cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/cloud-scripts-deployment-tool/) will not be signed with the Patch My PC code-signing certificate.

### Use Case 1: Intune Detection and Requirement Scripts

Specifically for Intune detection and requirement scripts, **AgentExecutor.exe** (the Intune client process responsible for calling Win32 app detection or requirement scripts) runs in session 0; it is not visible by the logged on user and PowerShell is awaiting input by the user to accept the code-signing certificate.

![](../../../.gitbook/assets/image-\(1832\).png)

After 60 minutes, the Intune Management Extension service will timeout and terminate the **powershell.exe** process with the below log entries in the **IntuneManagementExtension.log**.

> **Note**
>
> Microsoft do not expose this timeout to be configurable in Intune.

![](../../../.gitbook/assets/image-\(1833\).png)

### Use Case 2: Patch My PC Helper Scripts

PMPC utilizes "helper" scripts to perform both required and recommended pre/post actions for certain applications in the PMPC catalog. These helper scripts can, but are not limited to, help remove old versions of software if the vendor's installer does not handle this automatically.

### Deploying a certificate from Intune

You have two ways to deploy either certificate from Intune:

* [Using a Custom Configuration Policy](using-a-custom-configuration-policy-to-deploy-the-patch-my-pc-certificate.md) (recommended)
* [Using a script](using-a-script-to-deploy-the-patch-my-pc-certificate.md)

> **Note**
>
> If you prefer to deploy a certificate using a method not described here, you can download it from: [https://patchmypc.com/codesign](https://patchmypc.com/codesign)

> **Important**
>
> In addition, the computer must trust the certificate chain for the code-signing certificate, which is generally the case with certificates issued by public CAs. By importing the code-signing certificate's public key into the Trusted Publishers store, you ensure PowerShell can successfully verify and run the signed scripts.
