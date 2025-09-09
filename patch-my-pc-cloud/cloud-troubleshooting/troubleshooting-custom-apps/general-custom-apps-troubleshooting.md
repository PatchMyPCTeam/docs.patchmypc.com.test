# General Custom Apps Troubleshooting

_Applies to: Patch My PC (PMPC) Cloud Custom Apps_

If issues arise when deploy apps using Patch My PC (PMPC) Cloud Custom App deployments, please follow these initial troubleshooting steps:

* [Review Custom Apps Reference](general-custom-apps-troubleshooting.md#review-custom-apps-reference)
* [Check Installation Commands](general-custom-apps-troubleshooting.md#check-installation-commands)
* [Review the Considerations when using Custom Apps](general-custom-apps-troubleshooting.md#considerations)
* [Consult our List of Common Installation Switches](general-custom-apps-troubleshooting.md#list-of-common-installation-switches)
* [Test Locally](general-custom-apps-troubleshooting.md#test-locally)
* [Additional Troubleshooting Steps](general-custom-apps-troubleshooting.md#additional-troubleshooting-steps)

Please also consider the following when using the Custom Apps feature:

* [Support Limitations](general-custom-apps-troubleshooting.md#support-limitations)

### <strong>Review Custom Apps Reference:</strong>

Please review the [Custom Apps Reference](https://docs.patchmypc.com/installation-guides/patch-my-pc-cloud/custom-apps/custom-apps-reference) section.

### <strong>Check Installation Commands:</strong>

Verify you are using the correct commands, switches, and parameters:

* Consult vendor installation guides
* Review knowledge base or deployment documentation
* Resources:
  * [Silent Install HQ](https://silentinstallhq.com/)
  * [IT Ninja](https://www.itninja.com/)
  * [App Deploy News](https://appdeploynews.com/)&#x20;
* Try running the installer with the following common switches for guidance:\
  &#x20;`/?`, `-?`, `/h`, or `--help`&#x20;
* Extract the installer files to locate their documentation.
* Search vendor forums/support sites using "<strong>command line</strong>" terms.

### Considerations

* Apps must support silent install
* Per-user MSI’s are not currently supported
* Not all newer version of applications will automatically remove the existing version. Consider using the Patch My PC [Uninstall-Software.ps1](https://github.com/PatchMyPCTeam/Community-Scripts/tree/main/Uninstall/Pre-Uninstall/Uninstall-Software) community script as a [Pre-Install Script](../../cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/cloud-scripts-deployment-tool/#pre-install-script) in that scenario
* Putting the Architecture in the <strong>DisplayName</strong> forces detection to look in the <strong>64bit Uninstall ARP</strong> key - example: <strong>x64</strong> or <strong>64bit</strong> or <strong>64-bit</strong>
* Apps need a valid <strong>DisplayVersion</strong> for detection. For example, <strong>1.00-00e.2</strong> is not a valid version number
* Test the app installs okay as the <strong>SYSTEM</strong> user using [PsExec](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec). Intune will install apps in the <strong>SYSTEM</strong> context and this may affect installation and/or detection.

### <strong>List of Common Installation Switches</strong>

| Installer Technology | Silent/Quiet Install                 | Prevent Reboot                          |
| -------------------- | ------------------------------------ | --------------------------------------- |
| MSI                  | `/quiet` or `/q` or `/qn`            | `/norestart` or `REBOOT=ReallySuppress` |
| NSIS (Nullsoft)      | `/S` (case sensitive!)               |                                         |
| Inno Setup           | `/SP- /VERYSILENT /SUPPRESSMSGBOXES` | `/NORESTART`                            |
| InstallShield        | `/s` or `/s` or `/SMS`               |                                         |

### <strong>Test Locally</strong>

Use a checklist similar to that below, before deploying via PMPC Cloud to thoroughly test installations locally:

<table><thead><tr><th width="295">Test Case</th><th width="67">Pass</th><th width="56">Fail</th><th width="282">Notes</th></tr></thead><tbody><tr><td>Manual Installation</td><td>✔️</td><td></td><td> </td></tr><tr><td>Manual Uninstallation</td><td></td><td>❌</td><td> </td></tr><tr><td>User Prompt Verification</td><td></td><td></td><td>List prompts encountered</td></tr><tr><td>Silent Installation (/quiet /noreboot)</td><td></td><td></td><td> </td></tr><tr><td>Custom Pre-Installation Scripts</td><td></td><td></td><td> </td></tr><tr><td>Custom Post-Installation Scripts</td><td></td><td></td><td> </td></tr><tr><td>Application Launch After Install</td><td></td><td></td><td> </td></tr><tr><td>Installation on Clean System</td><td></td><td></td><td> </td></tr><tr><td>Installation over Previous Version</td><td></td><td></td><td> </td></tr><tr><td>Logging Verification</td><td></td><td></td><td> </td></tr><tr><td>Disk Space Requirements Check</td><td></td><td></td><td> </td></tr><tr><td>System Restart Behavior</td><td></td><td></td><td> </td></tr><tr><td>Installed as SYSTEM using psexec</td><td></td><td></td><td></td></tr></tbody></table>

### &#x20;<strong>Additional Troubleshooting Steps</strong>

* <strong>Review Logs:</strong> Examine vendor-specific logs for detailed error messages
* <strong>Simplify Installation:</strong> Divide complex installations into simpler steps to isolate issues.

### <strong>Support Limitations</strong>

As detailed in our [Custom Apps Support Statement](https://patchmypc.com/custom-apps-support-statement), full deployment support for every custom application cannot be assured. Some applications may:

* Use proprietary or unusual installation methods
* Require specific environmental configurations
* Need specialized knowledge from the vendor
* Employ installation technologies incompatible with our service.

#### &#x20;<strong>Our Support Team Can Help With:</strong>

* Initial setup of the Custom Apps feature
* Successful uploads of Custom Apps
* Verification that apps appear correctly for publishing in Patch My PC Publisher
* Uploading applications to the Custom Apps portal
* Connecting to the Patch My PC Publisher
* Resolving login and user invitation issues within the Custom Apps portal
* Addressing errors related to Custom Apps appearing in PatchMyPC.log or the Custom Apps UI.

#### <strong>"Best-Effort" Support Offered for Custom Apps that fail:</strong>

* Installation on devices
* To be detected post-installation.

#### <strong>Our Support Team Cannot:</strong>

* Guarantee packaging success for every application through the Custom Apps feature
* Create Custom Apps on behalf of customers
* Write custom scripts to facilitate app installations.

### <strong>Getting Support</strong>

Our team will support you within our capabilities, as outlined above.&#x20;

But, for highly specialized or complex apps, complete solutions may not always be possible. If an app issue falls beyond our scope, consider consulting directly with the application vendor.

To submit a support case concerning Custom Apps you, [Open a Support Case](https://patchmypc.com/technical-support) and choose “<strong>Custom Apps</strong>” as the product.