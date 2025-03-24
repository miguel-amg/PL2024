# Compiler Design

**Author:** Miguel Guimarães [(Github)](https://github.com/miguel-amg).

**University of Minho** - Bachelor's degree in Software Engineering

**Year 2024/2025**

# Assignment 2: MD to HTML Converter
1. Create a small MarkDown to HTML converter in Python for the elements described in the "Basic Syntax" Cheat Sheet:
    - **Headings:** lines starting with "# text", or "## text" or "### text"
        ```
        In: # Example
        Out: <h1>Example</h1>
        ```
    - **Bold:** pieces of text between "**":
      ```
        In: This is an **example** ...
        Out: This is an <b>example</b> ...
      ```
    - **Italics:** pieces of text between "*":
      ```
        In: This is an *example* ...
        Out: This is an <i>example</i> ...
      ```
    - **Numbered list:**
      ```
        In:
            1. First item
            2. Second item
            3. Third item
        Out:
            <ol>
                <li>First item</li>
                <li>Second item</li>
                <li>Third item</li>
            </ol>
       ```
    - **Link:** [text](URL address)
      ```
        In: As can be found at [UC website](http://www.uc.pt)
        Out: As can be found at <a href="http://www.uc.pt">UC website</a>
      ```
    - **Image:** ![alt text](path to image)
      ```
        In: As seen in the following image: ![image of a rabbit](http://www.rabbit.com) ...
        Out: As seen in the following image: <img src="http://www.rabbit.com" alt="image of a rabbit"/> ...
      ```
