# "Error - Downgrading from an MSP Plus license is currently not supported."

_Applies to: Patch My PC Cloud_

### SYMPTOMS

Why after downgrading my MSP Patch My PC (PMPC) Cloud license, do I get the following error?:

**Error**

**“Downgrading from an MSP Plus license is currently not supported. Please contact support@patchmypc.com for further assistance."**

!\[]\(/\_images/image-(2703 "").png "")

### CAUSE

You are seeing this error as we currently do not support downgrading an MSP license to a different license level, such as Enterprise Plus or Enterprise Premium.

### RESOLUTION

The workaround to this issue is:

1. [Remove all of the companies](../../managed-service-provider/managed-service-provider-administration/manage-msp-companies/remove-a-company-from-being-managed-cloud-msp.md) being managed by this MSP license.
2. [Delete the company](../../cloud-administration/manage-your-cloud-company/delete-your-cloud-company.md) you no longer wish to be an MSP.
3. [Onboard a new company](../../onboard-to-cloud.md) to PMPC Cloud.
4. Onboard the new company to [Intune Apps](../../intune-apps/onboard-to-intune-apps/) and use the new downgraded license.
