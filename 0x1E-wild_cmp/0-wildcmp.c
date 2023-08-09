#include "holberton.h"
/**
 * wildcmp - a function to compare two strings to
 * determin if they are exactly the same.
 * @s1: a string
 * @s2: a string that can contain the wildcard *
 * Return: 1 if exactly the same, 0 if not
 */
int wildcmp(char *s1, char *s2)
{
  if (*s1 == '\0' && *s2 == '\0')
    return (1);
  if (*s1 == '\0' && *s2 == '*')
    return (wildcmp(s1, s2 + 1));
  if (*s1 == *s2)
    return (wildcmp(s1 + 1, s2 + 1));
  if (*s2 == '*')
    return (wildcmp(s1, s2 + 1) || wildcmp(s1 + 1, s2));

  return (0);
}
