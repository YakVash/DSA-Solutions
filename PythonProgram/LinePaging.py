def fifo_page_replacement(pages, capacity) :
    
    print("=== FIFO Page Replacement ===")
    frame = [] # To store pages currently in memory
    page_faults = 0 # Counter for page faults

    for page in pages :

        # If page not in frame → page fault occurs
        if page not in frame :

            if len(frame) < capacity :

                frame.append(page)

            else :

                # Remove the oldest page (First In)
                frame.pop(0)
                frame.append(page)

            page_faults += 1

        # Display current frame state
        print(f"Page: {page} -> Frame: {frame}")

    print("\nTotal Page Faults (FIFO):", page_faults)

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2] # Reference string
capacity = 3 # Number of frames
print("Reference String:", pages)
print("Frame Size:", capacity, "\n")
fifo_page_replacement(pages, capacity)
