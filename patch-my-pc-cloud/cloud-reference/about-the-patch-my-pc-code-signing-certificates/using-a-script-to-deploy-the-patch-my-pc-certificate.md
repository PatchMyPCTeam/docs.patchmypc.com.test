# Using a script to deploy the Patch My PC certificate

_Applies to: Patch My PC Cloud_

By using a script to deploy the Patch My PC (PMPC) certificate, you can either deploy the certificate as a:

* [Platform script](using-a-script-to-deploy-the-patch-my-pc-certificate.md#using-a-platform-script)
* [Proactive remediation](using-a-script-to-deploy-the-patch-my-pc-certificate.md#using-a-proactive-remediation)

In environments where a company configures an all-signed PowerShell policy or enforces script signature checking on the Win32 app in the Intune admin center, all scripts must be signed by a trusted publisher. Our script helps import the required certificate into the Trusted Publisher store to ensure that scripts signed by PMPC can be executed without issues.

To deploy our code signing certificate using a script, first download our scripts from:

[https://github.com/PatchMyPCTeam/Community-Scripts/tree/main/Other/Code%20Signing](https://github.com/PatchMyPCTeam/Community-Scripts/tree/main/Other/Code%20Signing)

{% hint style="info" %}
**Note**

You can find out more details about these scripts and what they do by reviewing the [ReadMe.md](https://github.com/PatchMyPCTeam/Community-Scripts/tree/main/Other/Code%20Signing#readme) file included with the scripts.
{% endhint %}

### Certificates to Deploy

There are two distinct use cases in PMPC Cloud that require separate certificates:

1. [Intune Detection and Requirement Scripts](using-a-script-to-deploy-the-patch-my-pc-certificate.md#id-1.-deploy-the-certificate-use-to-sign-intune-detection-and-requirement-scripts)\
   Used to sign **Intune detection and requirement scripts** for Win32 applications published through PMPC Cloud.
2. [Patch My PC Helper Scripts](using-a-script-to-deploy-the-patch-my-pc-certificate.md#id-2.-deploy-the-certificate-use-to-sign-patch-my-pc-helper-scripts)\
   Used to sign required and recommended pre/post "helper" scripts for certain applications in the PMPC catalog. These helper scripts perform essential tasks such as stopping processes, uninstalling older software versions, or configuring application behavior during deployment to ensure successful app installation.

### 1. Deploy the Certificate use to sign Intune Detection and Requirement Scripts

To deploy our certificate using a script, follow [Create a script policy and assign it](https://learn.microsoft.com/en-us/mem/intune/apps/intune-management-extension#create-a-script-policy-and-assign-it) using the following values.

#### “Platform scripts” tab

<table><thead><tr><th width="72">Field</th><th width="193">Value</th></tr></thead><tbody><tr><td>Add</td><td>Windows 10 and later</td></tr></tbody></table>

#### “Basics” tab

<table><thead><tr><th width="121">Field</th><th>Value</th></tr></thead><tbody><tr><td>Name</td><td>A descriptive name for the policy. E.g. “Patch My PC Cloud Trusted Publisher Certificate”`</td></tr><tr><td>Description</td><td>Enter an optional description for the policy</td></tr></tbody></table>

#### “Script Settings” tab

<table><thead><tr><th width="369">Field</th><th>Value</th></tr></thead><tbody><tr><td>Script location</td><td>Browse to and select <strong>Import-PMPCCloudTrustedPublisherCertificate.ps1</strong></td></tr><tr><td>Run this script using the logged on credentials</td><td>No</td></tr><tr><td>Enforce script signature check</td><td>No</td></tr><tr><td>Run script in 64 bit PowerShell Host</td><td>No</td></tr></tbody></table>

#### “Scope tags” tab

Configure as required.

#### “Assignments” tab

Assign the configuration template to the desired Entra ID group(s).

#### “Review + add” tab

Double-check everything before clicking **Add**.

### 2. Deploy the Certificate use to sign Patch My PC Helper Scripts

To deploy our certificate using a script, follow the [Create a script policy and assign it](https://learn.microsoft.com/en-us/mem/intune/apps/intune-management-extension#create-a-script-policy-and-assign-it) article using the following values.

#### “Platform scripts” tab

<table><thead><tr><th width="85">Field</th><th width="195">Value</th></tr></thead><tbody><tr><td>Add</td><td>Windows 10 and later</td></tr></tbody></table>

#### “Basics” tab

<table><thead><tr><th width="132">Field</th><th>Value</th></tr></thead><tbody><tr><td>Name</td><td>A descriptive name for the policy. E.g. “Patch My PC Apps Trusted Publisher Certificate”`</td></tr><tr><td>Description</td><td>Enter an optional description for the policy</td></tr></tbody></table>

#### “Script Settings” tab

<table><thead><tr><th width="305">Field</th><th>Value</th></tr></thead><tbody><tr><td>Script location</td><td>Browse to and select <strong>Import-PMPCAppsTrustedPublisherCertificate.ps1</strong></td></tr><tr><td>Run this script using the logged on credentials</td><td>No</td></tr><tr><td>Enforce script signature check</td><td>No</td></tr><tr><td>Run script in 64 bit PowerShell Host</td><td>No</td></tr></tbody></table>

#### “Scope tags” tab

Configure as required.

#### “Assignments” tab

Assign the configuration template to the desired Entra ID group(s).

#### “Review + add” tab

Double-check everything before clicking **Add**.

### Post Processing

You can see the script being processed by the Intune Management Extension by looking in the **IntuneManagementExtension.log** located at:

```
%ProgramData%\Microsoft\IntuneManagementExtension\Logs
```

<figure><img src="../../../_images/gitbook/image (648).png" alt="“IntuneManagementExtension.log” showing the script being processed by the Intune Management Extension" width="563"><figcaption></figcaption></figure>

### Using a proactive remediation

To deploy our certificate using a proactive remediation deployment, follow the [Remediations](https://learn.microsoft.com/en-us/mem/intune/fundamentals/remediations) article. The Remediation detection scripts can be found in the following repoistory on GitHub [https://github.com/PatchMyPCTeam/Community-Scripts/tree/main/Other/Code%20Signing](https://github.com/PatchMyPCTeam/Community-Scripts/tree/main/Other/Code%20Signing)

#### 1. Deploy the Certificate use to sign Intune Detection and Requirement Scripts

#### “Basics” tab

<table><thead><tr><th width="115">Field</th><th width="414">Value</th></tr></thead><tbody><tr><td>Name</td><td>A descriptive name for the policy. E.g. “Patch My PC Cloud Trusted Publisher Certificate”`</td></tr><tr><td>Description</td><td>Enter an optional description for the policy.</td></tr><tr><td>Publisher</td><td>Enter “Patch My PC”</td></tr></tbody></table>

#### “Settings” tab

<table><thead><tr><th width="291">Field</th><th>Value</th></tr></thead><tbody><tr><td>Detection script file</td><td>Browse to and select <strong>PMPCCloudTrustedPublisherCertificate_HealthScript_Detection.ps1</strong></td></tr><tr><td>Remediation script file</td><td>Browse to and select Import-<strong>PMPCCloudTrustedPublisherCertificate.ps1</strong></td></tr><tr><td>Run this script using the logged on credentials</td><td>No</td></tr><tr><td>Enforce script signature check</td><td>No</td></tr><tr><td>Run script in 64 bit PowerShell Host</td><td>No</td></tr></tbody></table>

#### &#x20;“Scope tags” tab

Configure as required.

#### “Assignments” tab

Assign the configuration template to the desired Entra ID group(s), then configure the frequency you want the Proactive Remediation to be executed on the targeted devices.

#### “Review + create” tab

Double-check everything before clicking **Create**.

#### 2. Deploy the Certificate use to sign Patch My PC Helper Scripts

#### “Basics” tab

<table><thead><tr><th width="118">Field</th><th>Value</th></tr></thead><tbody><tr><td>Name</td><td>A descriptive name for the policy. E.g. “Patch My PC Apps Trusted Publisher Certificate”`</td></tr><tr><td>Description</td><td>Enter an optional description for the policy.</td></tr><tr><td>Publisher</td><td>Enter “Patch My PC”</td></tr></tbody></table>

#### “Settings” tab

<table><thead><tr><th width="290">Field</th><th>Value</th></tr></thead><tbody><tr><td>Detection script file</td><td>Browse to and select <strong>PMPCAppsTrustedPublisherCertificate_HealthScript_Detection.ps1</strong></td></tr><tr><td>Remediation script file</td><td>Browse to and select Import-<strong>PMPCAppsTrustedPublisherCertificate.ps1</strong></td></tr><tr><td>Run this script using the logged on credentials</td><td>No</td></tr><tr><td>Enforce script signature check</td><td>No</td></tr><tr><td>Run script in 64 bit PowerShell Host</td><td>No</td></tr></tbody></table>

#### &#x20;“Scope tags” tab

Configure as required.

#### “Assignments” tab

Assign the configuration template to the desired Entra ID group(s), then configure the frequency you want the Proactive Remediation to be executed on the targeted devices.

#### “Review + create” tab

Double-check everything before clicking **Create**.

#### Post Processing

You can see the script being processed by the Intune Management Extension by looking in the **HealthScriptss.log** located at:

```
%ProgramData%\Microsoft\IntuneManagementExtension\Logs
```

Observe the **Proactive Remediation Device Status** blade.

<figure><img src="../../../_images/gitbook/image (649).png" alt="Observing the “Proactive Remediation Device Status” blade." width="563"><figcaption></figcaption></figure>

The following log snippet shows the **HealthScripts.log** entry if the pre-remediation (detection) script found the certificate already installed in the local computer’s Trusted Publishers store.

<figure><img src="../../../_images/gitbook/image (650).png" alt="“HealthScripts.log” snippet showing if the pre-remediation (detection) script has found the certificate already installed in the local machine’s Trusted Publishers store." width="563"><figcaption></figcaption></figure>

The following log snippet shows the **HealthScripts.log** entry if the pre-remediation (detection) script did not find the certificate already installed in the local machine’s Trusted Publishers store (the Exit code of the script is **1**).

<figure><img src="../../../_images/gitbook/image (651).png" alt="“HealthScripts.log” snippet showing if the pre-remediation (detection) script did not find the certificate already installed in the local machine’s Trusted Publishers store (the Exit code of the script is 1)." width="563"><figcaption></figcaption></figure>

The following log snippet shows the **HealthScripts.log** entry if the pre-remediation (detection) script did not find the certificate already installed in the local machine’s Trusted Publishers store and the remediation script was run successfully (Exit code of the script is **0**).

<figure><img src="../../../_images/gitbook/image (652).png" alt="“HealthScripts.log” snippet showing the pre-remediation (detection) script did not find the certificate already installed in the local machine’s Trusted Publishers store and the remediation script was run successfully (Exit code of the script is 0)." width="563"><figcaption></figcaption></figure>
