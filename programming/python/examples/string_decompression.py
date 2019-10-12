import time


def decompress(string):
    """
    Without recursion using a stack
    """

    stack = []
    text = ""
    for c in string:

        if c.isdigit():
            c = int(c)
            if len(stack) > 0:
                t = stack[-1]
                if isinstance(t, int):  # handle numbers with multiple digits
                    stack[-1] = stack[-1] * 10 + c
                    continue
            stack.append(c)  # only one number

        elif c == "]":  # evaluate the closed term
            s = ""
            while True:  # pop every item until the opening bracket is reached
                x = stack.pop()

                if x == "[":
                    i = stack.pop()
                    stack += ((i * s)[::-1])  # concat stack with evaluated term
                    break
                else:
                    s += x

        else:
            stack.append(c)  # push to stack

    if len(stack) > 0:
        text += "".join(stack)

    return text


def decomp_by_google(text, start=0, times=1):
    """
    Example solution by google.
    Iterate over and decompress the compressed string.
    This approach makes use of nested Python iterators, which is a very clean way
    of expressing expansion of nested iterated items.
    Args:
        text: The entire string to decompress.  It's unobvious, but nice
          to have the whole string plus an index; this allows any error
          detection code to report the absolute index of a problematic
          character.
        start: The starting index within 'text'.  We decompress from
          'start' up through the matching close-brace or end-of-string.
        times: The number of times to repeat decompression.
    """
    # Repeat iteration over our sub-chunk N times.
    for _ in xrange(times):
        i = start
        # Until we hit the end of the string, or end of our chunk...
        while i < len(text) and text[i] != ']':
            # Emit letters as themselves.#
            if text[i].islower():
                yield text[i]
            # If it's not a letter, it must be digit(s).  Convert to integer.
            else:
                sub_times = 0
                while text[i].isdigit():
                    sub_times = sub_times * 10 + int(text[i])
                    i += 1
                i += 1  # Skip past open-bracket
                # Start an iterator over the sub-chunk.
                for item in decomp_by_google(text, i, sub_times):
                    # Iterator generates many characters, and then at the very end,
                    # it generates an integer.  Provide characters up to our caller,
                    # and use the integer to advance our index 'i' to end-of-chunk.
                    if isinstance(item, basestring):
                        yield item
                    else:
                        i = item
                # Advance 'i' to the next letter, or skip the close-bracket, whichever.
            i += 1
        # Don't emit the trailing integer if we are doing the outermost call.  This
        # test could be moved to the decompress() call instead; we would check there
        # to see if the result item was basestring or int, just as we do above, but
        # I suspect that check would be more expensive than a simple integer
        # comparison here, where the type is known.
        if start > 0:
            yield i


def test(tests):
    def run_test(instance):
        return decompress(instance[0]) == instance[1]

    start = time.time()
    r = [run_test(t) for t in tests]

    return r, time.time() - start


def test_google(tests):
    def run_test(instance):
        return "".join(decomp_by_google(instance[0])) == instance[1]

    start = time.time()
    r = [run_test(t) for t in tests]

    return r, time.time() - start


tests = [("3[AB2[CD]]".lower(), "ABCDCDABCDCDABCDCD".lower()),
         ("3[abc]4[ab]c", "abcabcabcababababc"),
         ("", ""),
         ("3[2[1[A]]]".lower(), "AAAAAA".lower()),
         ("15[A]".lower(), 15 * "A".lower()),
         ("5[a]", "aaaaa"),
         ("aaa", "aaa"),
         ("10[a]", "aaaaaaaaaa"),
         ("2[aabc]d", "aabcaabcd"),
         ("2[2[abbb]c]", "abbbabbbcabbbabbbc"),
         (99999 * "1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[xx]]]]]]]]]]]]]]]]]]]]", "xx")]

print(test(tests))  # takes 3.84 secs (on a core i5)
print(test_google(tests))  # takes 3.57 secs (on a core i5)

