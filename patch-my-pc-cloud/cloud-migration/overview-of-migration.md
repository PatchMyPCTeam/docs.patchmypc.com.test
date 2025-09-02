# Overview of Migration

_Applies to: Patch My PC Cloud_

{% hint style="danger" %}
**Important**

This feature is currently only available through an invitation-only Private Preview, as both it and the documentation are under development, incomplete, and subject to change.

Please do not share links to these docs with others outside of the Private Preview.

Once this feature is released, it will be announced and this banner removed.
{% endhint %}

The _Migration_ feature of Patch My PC (PMPC) Cloud allows you to migrate the following items from a Microsoft Configuration Manager (ConfigMgr) hierarchy to a PMPC Cloud company:

* [Applications](overview-of-migration.md#migrating-applications)

{% hint style="info" %}
**Note**

We are currently focusing on just application migration, but we do plan to add the ability to migrate other types of objects from ConfigMgr as the Migration feature evolves.
{% endhint %}

### Migrating Applications

The _Migration_ feature is designed to support the migration of applications from Microsoft Configuration Manager (ConfigMgr) to Microsoft Intune, with a focus on modernization rather than simply transferring technical debt.

As part of the migration process, we want to help you identify outdated applications or those exposed to known Common Vulnerabilities and Exposures (CVEs). We will also make recommendations and assist in upgrading to the latest supported, secure versions available through the Patch My PC Catalog.

All applications we migrate will benefit from an additional layer of customization to ensure they remain manageable, secure and fit for the modern desktop.

We have two approaches for migrating applications from ConfigMgr to Intune:

* [Publish the App in Intune as a PMPC App](overview-of-migration.md#publish-the-app-in-intune-as-a-pmpc-app)
* [Publish the App in Intune as a PMPC Custom App](overview-of-migration.md#publish-the-app-in-intune-as-a-pmpc-custom-app)

#### Publish the App in Intune as a PMPC App

Wherever possible, we try to find a match for ConfigMgr applications to an app that already exists in our catalog, using various methods and metadata. If a match is found, you can then deploy this version to Intune rather than the older version, which may be vulnerable to exploits, out of support, etc.

When we migrate ConfigMgr applications using this method, we include the migration of any installation arguments, customizations, and command lines you have in the ConfigMgr application.

The end result is that you now have a version of the app deployed that can be managed and kept up to date for the life of that app.

#### Publish the App in Intune as a PMPC Custom App

For those ConfigMgr applications that we cannot find a direct match to a version in our catalog, we can still migrate it, but as a [PMPC Custom App](../custom-apps/custom-apps-overview.md). None of the properties, versions or other settings of the existing ConfigMgr application will be modified, but you will be able to modify and manage the app from within the PMPC Cloud portal and take advantage of the various customizations and features of PMPC Cloud Custom Apps.