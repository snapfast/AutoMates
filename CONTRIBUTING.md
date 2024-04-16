# How to contribute

Support and contributions from the open source community are essential for keeping
`@snapfast/AutoMates` up to date and always improving! There are a few guidelines that we need
contributors to follow to keep the project consistent, as well as allow us to keep
maintaining `@snapfast/AutoMates` in a reasonable amount of time.

Please note that this project is released with a [Contributor Code of Conduct][coc].
By participating in this project you agree to abide by its terms.

[coc]: ./CODE_OF_CONDUCT.md

## Creating an Issue

Before you create a new Issue:

1. Please make sure there is no [open issue](https://github.com/snapfast/automates/issues) yet.
2. If it is a bug report, include the steps to reproduce the issue and please create a reproducible test case on [runkit.com](https://runkit.com/). Example: https://runkit.com/gr2m/5aa034f1440b420012a6eebf
3. If it is a feature request, please share the motivation for the new feature and how you would implement it.
4. Please include links to the corresponding github documentation.

## Tests

If you want to submit a bug fix or new feature, make sure that all tests are passing.

```
$ python run.py
```

If anyone wants to introduce testing into this project, you are welcome. Send me a pull request for testing these features.

## Making Changes

Here is an overview

- Create a topic branch from the main branch.
- Check for unnecessary whitespace / changes with `git diff --check` before committing.
- Keep git commit messages clear and appropriate. Ideally follow commit conventions described below.

## Submitting the Pull Request

- Push your changes to main branch on your fork of the repo, since this project is closely monitored.
- If you are making a change that is architecturally different, then submit a pull request from your topic branch like `Functional Programming`.
- Be sure to tag any issues your pull request is taking care Code of Conduct.

## Testing a pull request from github repo locally:

Before submitting any pull request, make sure the code is running for you locally. If the pull request looks good but does not follow the commit conventions, use the "Squash & merge" button.
