Hijack Checker
========================================

Note: these instructions are super verbose because they were written for people with little Python or DNS experience.

What problem does this solve?
----------------------------------------
***Subdomain hijacking*** is a widespread issue currently. Essentially, domain owners use
3rd-party providers to host content by redirecting users via DNS CNAME records. However,
when those domains are no longer used, they frequently cancel the 3rd-party provider without
deleting that CNAME record. If an attacker manages to discover this unused CNAME record, via either
a subdomain bruteforcing approach or via a DNS zone transfer, they can register an instance with that
3rd-party host with the same name; this will allow them to host their own content on the domain being
attacked.

Why did this tool get written?
----------------------------------------

There are existing tools that purport to do this automatically, but they generate a bunch of false positives.
In one case, it would *only* generate false positives and skip over valid hijack domains entirely. This tool at
least, in my limited testing, can tell reliably if a subdomain is vulnerable to hijacking.


Installation instructions
----------------------------------------

  1. Make sure you have `python3` and `pip3` installed and in your path.
  2. Clone this repository
  3. `cd` to your freshly-created repository directory
  4. Install the package by `pip3 install .`
  
  
Usage instructions
----------------------------------------

Run the program via `hijack-checker <domain>`. It will output "HIJACK" if the domain is vulnerable, and "Clear" if
the domain either doesn't exist or points to a valid host.

Suggested workflow: discover a list of subdomains using [SubBrute](https://github.com/TheRook/subbrute) or some other
domain enumeration tool. You can then feed this list into hijack-checker using `xargs` or your scripting language
of choice.
