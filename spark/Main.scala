// Main entry point for the Spark conversion project

object Main {
  def main(args: Array[String]): Unit = {
    println("Starting Pharma Bricks Spark Conversion...")
    
    try {
      // Run CSVConversion directly
      CSVConversion.main(args)
    } catch {
      case e: Exception =>
        println(s"Error running CSVConversion: ${e.getMessage}")
        e.printStackTrace()
    }
  }
}
