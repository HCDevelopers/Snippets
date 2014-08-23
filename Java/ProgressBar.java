package snippets;

/**
 * Animated progress bar for CLI applications
 * <p>
 * Comes in handy for command line tools that need to show a progress. It uses
 * carriage return character (/r) to move the cursor back to the beginning of
 * the current line thus overwriting the content afterwards. This way it can
 * show a progress animation.
 * 
 * @author Deque
 * 
 */
public class ProgressBar {

	private final int width;
	private String barStart = "[";
	private String barEnd = "]";
	private String arrowBody = "=";
	private String arrowEnd = ">";

	/**
	 * Instantiate progress bar with width
	 * 
	 * @param width
	 *            width in characters
	 */
	public ProgressBar(int width) {
		this.width = width;
	}

	/**
	 * Instantiate progress bar with width and looks of the bar's elements
	 * 
	 * @param width
	 *            width in characters
	 * @param barStart
	 *            left side of the bar
	 * @param barEnd
	 *            right side of the bar
	 * @param arrowBody
	 *            the characters that make up the body of the arrow
	 * @param arrowEnd
	 *            the characters that make up the end of the arrow
	 */
	public ProgressBar(int width, String barStart, String barEnd,
			String arrowBody, String arrowEnd) {
		this.barStart = barStart;
		this.barEnd = barEnd;
		this.arrowBody = arrowBody;
		this.arrowEnd = arrowEnd;
		this.width = width;
	}

	/**
	 * Returns to the beginning of the line and prints the progress bar for
	 * given percentage to stdout.
	 * 
	 * @param percent
	 *            percentage shown by the progress bar
	 */
	public void printProgressBar(int percent) {
		int processWidth = percent * width / 100;
		System.out.print("\r" + barStart);
		for (int i = 0; i < processWidth; i++) {
			System.out.print(arrowBody);
		}
		System.out.print(arrowEnd);
		for (int i = processWidth; i < width; i++) {
			System.out.print(" ");
		}
		System.out.print(barEnd + percent + "%");
	}

	/**
	 * Usage example. Note: Use a real terminal for testing, not an IDE. E.g. it
	 * doesn't work with the Eclipse Console.
	 * 
	 * @param args
	 * @throws InterruptedException
	 */
	public static void main(String[] args) throws InterruptedException {
		ProgressBar bar = new ProgressBar(50);
		for (int i = 0; i <= 10; i++) {
			Thread.sleep(600);
			bar.printProgressBar(i * 10);
		}
		System.out.println();
	}

}
