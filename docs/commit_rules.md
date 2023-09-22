# Commit Rules

## Example Commit Message

```
init   (hw_3):    add solutions for tasks
<type> (<scope>):  <short summary>
  │       │             │
  │       │             └─⫸ Summary in present tense. Not capitalized. No period at the end.
  │       │
  │       └─⫸ Commit Scope: hw_1|hw_2|hw_3|hw_4|hw_5
  │
  └─⫸ Commit Type: build|docs|feat|fix|perf|refactor|test|init
```

## Principles

- 盡量讓 Commit 單一化，一次只更動一個主題
- **標題的動詞統一用過去式！！！**

## Type

- **build**
  - modification of the build system or external dependencies
- **docs**
  - documentation
  - **docs.add**
  - **docs.update**
  - **docs.fix**
- **feat**
  - new feature
- **fix**
  - bug fix
- **perf**
  - 改善效能 (A code change that improves performance)
- **style**
  - 格式 (不影響程式碼運行的變動 white-space, formatting, missing semi colons, etc)
- **refactor**
- **test**
- **init**
  - start project/task
- **revert**
- **chore**
  - 建構程序或輔助工具的變動 (maintain)