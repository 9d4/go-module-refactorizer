# go-module-refactorizer

This tool is used to refactor module imports inside `.go` files in directory. See below.

Before:
```go
import (
	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api/v5"
	"github.com/traperwaze/ampastelobot/action"
	"github.com/traperwaze/ampastelobot/session"
)
```

After:
```go
import (
	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api/v5"
	"github.com/9d4/ampastelobot/action"
	"github.com/9d4/ampastelobot/session"
)
```

So, in demo above, I changed the `github.com/traperwaze` to `github.com/9d4`.

# Usage
I know this is the part you want to find the most. It's very simple to use this tool.
This tool is written in python. I've tested with python3, I don't know if it will work 
with python2 or not, you may give it a try.

```shell
$ python3 main.py dir old_name new_name
```

Anything wrong? Don't hesitate to make issue or pull request.
