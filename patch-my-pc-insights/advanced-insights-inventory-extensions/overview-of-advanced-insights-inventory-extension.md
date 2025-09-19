---
description: Technical detail for the Inventory Extensions
---

# Overview of Advanced Insights Inventory Extension

_Applies to: Patch My PC Advanced Insights_

## Inventory Extensions Process Visualized

![](/_images/WMI-(1).png "")

## What is the Inventory Extensions MSI?

The Inventory Extensions MSI is a .NET <strong>WMI Provider</strong>. This provider code is loaded by the <strong>WMI Service</strong> on Windows clients. The provider returns data that the client processes into a hardware inventory report where it is then submitted to the ConfigMgr site server and entered into the SQL database.

## What is WMI?

<strong>WMI</strong> stands for <strong>Windows Management Instrumentation</strong>. It is a set of specifications from Microsoft for consolidating the management of devices and applications in a network from Windows-based systems. WMI provides a standardized way for systems administrators to manage and query information about their systems.

The heart of <strong>WMI</strong> is the <strong>WMI Service</strong>, known as `Winmgmt` and part of the Windows OS, this service runs in the background on all Windows systems. This service acts as a broker between <strong>WMI Clients</strong> (ConfigMgr client) and the <strong>WMI Providers</strong> (Inventory Extensions MSI) that deliver the actual data.

## How does this integrate with ConfigMgr?

ConfigMgr's existing hardware inventory data is collected from <strong>WMI</strong>. We simply extend ConfigMgr's default hardware inventory policy with the new definitions of our Inventory Extensions data. This allows the ConfigMgr clients to query our <strong>WMI Provider</strong> through the <strong>WMI Service</strong> during its normal hardware inventory task - just like it would for any existing hardware inventory class.

For this reason <strong>we do not consider the Inventory Extensions MSI as an "Agent"</strong>. We do not install any services on clients, instead the existing WMI Service brokers the connection between our Inventory Extension MSI code and the ConfigMgr client for us. The only time this code runs on clients is during a Hardware Inventory task or when a custom client action is invoked, after which the <strong>WMI Service</strong> handles the unloading of our <strong>WMI Provider</strong>.