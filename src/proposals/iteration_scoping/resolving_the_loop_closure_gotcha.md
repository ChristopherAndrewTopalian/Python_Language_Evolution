## Resolving the Loop-Closure "Gotcha": A Path Toward Intuitive Binding

**To the Python Steering Council and Core Developers,**

Python has won the world over by being the most readable, intuitive, and beginner-friendly language in existence. When a new programmer writes Python, the language usually behaves exactly how human logic expects it to.

However, there is one glaring exception that continues to act as a massive barrier for beginners and a frustrating quirk for veterans: **late binding in loop closures.**

When a beginner writes a natural, logical loop to generate callbacks or lambdas, they expect this to work:

```python
buttons = []
for person in ["Alice", "Bob", "Charlie"]:
    buttons.append(lambda: print(f"Clicked {person}"))

```

Instead of printing Alice, Bob, and Charlie, every button prints "Charlie."

To explain *why* this happens, we have to pause a beginner's education to teach them about execution contexts, namespace references, and late binding. But more importantly, the accepted workaround violates several core tenets of the Zen of Python.

### The Un-Pythonic Workaround

The standard solution is to trap the variable as a default argument:

```python
buttons.append(lambda p=person: print(f"Clicked {p}"))

```

This workaround is clever, but it is deeply un-Pythonic.

1. **It violates "Readability counts":** `lambda p=person:` looks like arcane boilerplate to a beginner. It clutters the code with artificial parameters that are never actually passed by the caller.
2. **It violates "Simple is better than complex":** We are forcing developers to exploit a quirk of function-definition time just to bypass a quirk of loop-closure time.
3. **It violates "Explicit is better than implicit":** The developer is forced to implicitly hide a loop variable inside a default argument to freeze its state.

For developers coming from JavaScript (post-ES6) or C#, this feels like a massive step backward in a language that otherwise champions elegance.

### A Blueprint for Change

We understand that Python does not have block scope, and introducing a new keyword like `let` would fracture the language's variable assignment philosophy. Furthermore, silently changing how `for` loops bind variables would break backward compatibility for codebases that rely on the current late-binding behavior.

However, other mature languages have successfully navigated this exact migration. In C# 5.0, the language designers recognized that their `foreach` loop closure behavior was a trap for developers. They made the bold choice to change the iteration variable to capture by value per iteration, acknowledging it as a breaking change but deciding the long-term usability was worth it.

Python has the tooling to do this elegantly.

Could we begin a discussion on introducing a `__future__` import (e.g., `from __future__ import iteration_scoping`) that changes `for` loop variables to bind natively per-iteration when captured by a closure?

By providing a transition path, we can eventually eradicate this "gotcha." Doing so would remove one of the last major syntactic roadblocks for beginners, provide a superpower for readability, and align loop closures with the intuitive nature that makes Python wonderful.

Kind Regards  
Christopher Andrew Topalian  

---

// Dedicated to God the Father  
// (c) Copyright 2026 Christopher Andrew Topalian All Rights Reserved  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

