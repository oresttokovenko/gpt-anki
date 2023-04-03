import os
import openai

# MODIFY: Replace the following placeholder input with your own implementation to generate flash card question and answers

input = """
Modern applications require a high degree of parallelism. Even a very single-minded application can have a complex user interface—which requires concurrent activities. As machines get faster, users become more sensitive to waiting for unrelated tasks that seize control of their time. Threads provide efficient multiprocessing and distribution of tasks for both client and server applications. Java makes threads easy to use because support for them is built into the language.

Concurrency is nice, but there’s more to programming with threads than just performing multiple tasks simultaneously. In most cases, threads need to be synchronized (coordinated), which can be tricky without explicit language support. Java supports synchronization based on the monitor and condition model—a sort of lock and key system for accessing resources. The keyword synchronized designates methods and blocks of code for safe, serialized access within an object. There are also simple, primitive methods for explicit waiting and signaling between threads interested in the same object.

Java also has a high-level concurrency package that provides powerful utilities addressing common patterns in multithreaded programming, such as thread pools, coordination of tasks, and sophisticated locking. With the addition of the concurrency package and related utilities, Java provides some of the most advanced thread-related utilities of any language.

Although some developers may never have to write multithreaded code, learning to program with threads is an important part of mastering programming in Java and something all developers should grasp. See Chapter 9 for a discussion of this topic.

Scalability

At the lowest level, Java programs consist of classes. Classes are intended to be small, modular components. Over classes, Java provides packages, a layer of structure that groups classes into functional units. Packages provide a naming convention for organizing classes and a second tier of organizational control over the visibility of variables and methods in Java applications.

Within a package, a class is either publicly visible or protected from outside access. Packages form another type of scope that is closer to the application level. This lends itself to building reusable components that work together in a system. Packages also help in designing a scalable application that can grow without becoming a bird’s nest of tightly coupled code. The reuse and scale issues are really only enforced with the module system (again, added in Java 9), but that is beyond the scope of this book
"""

# DO NOT MODIFY

confirmation = """
I have learned how to create flashcards. Please provide me with the text and I will output in a question/answer format in csv in a code block.
"""

# DO NOT MODIFY

prompt = """
I want you to act as a professional flashcard creator, able to create flashcards from the text I provide. Regarding the formulation of the card content, you stick to two principles: First, minimum information principle: The material you learn must be formulated in as simple way as it is only possible. Simplicity does not have to imply losing information and skipping the difficult part. Second, optimize wording: The wording of your items must be optimized to ensure that in minimum time the right bulb in your brain lights up. This will reduce error rates, increase specificity, reduce response time, and help your concentration. The following is a model card-create template for you to study. Text: The characteristics of the Dead Sea: Salt lake is located on the border between Israel and Jordan. Its shoreline is the lowest point on the Earth's surface, averaging 396 m below sea level. It is 74 km long. It is seven times as salty (30% by volume) as the ocean. Its density keeps swimmers afloat. Only simple organisms can live in its saline waters. Create cards based on the above text as follows: "Where is the Dead Sea located?", "on the border between Israel and Jordan." "What is the lowest point on the Earth's surface?", "The Dead Sea shoreline." "What is the average level on which the Dead Sea is located?", "400 meters (below sea level)." "How long is the Dead Sea?", "70 km." "How much saltier is the Dead Sea as compared with the oceans?", "7 times." "What is the volume content of salt in the Dead Sea?", "30%" "Why can the Dead Sea keep swimmers afloat?", "due to high salt content." "Why is the Dead Sea called Dead?", "Because only simple organisms can live in it" "Why only simple organisms can live in the Dead Sea?", "because of high salt content" Please output the flashcards you create as csv in a code block. If you have mastered it, please reply, "I have learned how to create flashcards. Please provide me with the text and I will output in a question/answer format in csv in a code block".
"""

def generate_chat_response(prompt, confirmation, input):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": confirmation},
                {"role": "user", "content": input}
            ],
            temperature=0.9,
            max_tokens=1500,
            top_p=0.5,
            frequency_penalty=2,
            presence_penalty=1.
        )

        output = (response['choices'][0]['message']['content'])
        return output

    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return None


response = generate_chat_response(prompt=prompt, confirmation=confirmation, input=input)
print(response)

# NOTE: copy and paste the response output into /csv/<your_deck.csv>