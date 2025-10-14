Dealing with the onslaught of Hacktoberfest
* https://hacktoberfest.com

Each year, October brings a swarm of new contributors participating in Hacktoberfest.  This event has its pros and cons, but it presents a monumental workload for the few active maintainers of this repo.  The maintainer workload is further impacted by a new version of CPython being released in the first week of each October.

To help make our algorithms more valuable to visitors, our CONTRIBUTING.md file outlines several strict requirements, such as tests, type hints, descriptive names, functions, and/or classes. Maintainers reviewing pull requests should try to encourage improvements to meet these goals, but when the workload becomes overwhelming (esp. in October), pull requests that do not meet these goals should be closed.

Below are a few [`gh`](https://cli.github.com) scripts that should close pull requests that do not match the definition of an acceptable algorithm as defined in CONTRIBUTING.md.  I tend to run these scripts in the following order.

* close_pull_requests_with_require_descriptive_names.sh
* close_pull_requests_with_require_tests.sh
* close_pull_requests_with_require_type_hints.sh
* close_pull_requests_with_failing_tests.sh
* close_pull_requests_with_awaiting_changes.sh
* find_git_conflicts.sh

### Run on 14 Oct 2025: 107 of 541 (19.77%) pull requests closed.

Script run | Open pull requests | Pull requests closed
--- | --- | ---
None | 541 | 0
require_descriptive_names | 515 | 26
require_tests | 498 | 17
require_type_hints | 496 | 2
failing_tests | 438 | ___58___
awaiting_changes | 434 | 4
git_conflicts | [ broken ] | 0
